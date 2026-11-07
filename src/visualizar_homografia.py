import cv2
import numpy as np
from ultralytics import YOLO

from chess_inference_example import (
    extract_raw_corner_centers,
    cluster_points,
    select_best_4
)

# ==========================================
# 1. CONFIGURACIÓN
# ==========================================

imagen_path = "datos/imagenes/chess_board_image.jpg"
modelo_esquinas = "models/corner_best.pt"

warp_size = 800

# ==========================================
# 2. CARGAR IMAGEN Y MODELO
# ==========================================

imagen = cv2.imread(imagen_path)

if imagen is None:
    raise FileNotFoundError(
        f"No se ha podido abrir {imagen_path}"
    )

modelo = YOLO(modelo_esquinas)

# ==========================================
# 3. DETECTAR ESQUINAS
# ==========================================

puntos, confianzas = extract_raw_corner_centers(
    modelo,
    imagen_path,
    conf_threshold=0.25
)

print("\nESQUINAS DETECTADAS:")
print(puntos)

# ==========================================
# 4. AGRUPAR ESQUINAS CERCANAS
# ==========================================

puntos_unicos, confianzas_unicas = cluster_points(
    puntos,
    confianzas,
    tol=150.0
)

print("\nESQUINAS TRAS AGRUPACIÓN:")
print(puntos_unicos)

# ==========================================
# 5. CALCULAR HOMOGRAFÍA
# ==========================================

error, H, perm, combo, pts4 = select_best_4(
    puntos_unicos,
    warp_size=warp_size
)

print("\nERROR DE REPROYECCIÓN:")
print(error)

print("\nPERMUTACIÓN SELECCIONADA:")
print(perm)

print("\nESQUINAS UTILIZADAS:")
print(pts4)

# ==========================================
# 6. TRANSFORMAR LA IMAGEN
# ==========================================

tablero_transformado = cv2.warpPerspective(
    imagen,
    H,
    (warp_size, warp_size)
)

# ==========================================
# 7. DIBUJAR CUADRÍCULA
# ==========================================

tam_casilla = warp_size // 8

for i in range(9):

    x = i * tam_casilla
    y = i * tam_casilla

    cv2.line(
        tablero_transformado,
        (x, 0),
        (x, warp_size),
        (0, 255, 0),
        2
    )

    cv2.line(
        tablero_transformado,
        (0, y),
        (warp_size, y),
        (0, 255, 0),
        2
    )

# ==========================================
# 8. DIBUJAR COORDENADAS DE LAS CASILLAS
# ==========================================

for fila in range(8):
    for columna in range(8):

        letra = chr(ord("a") + fila)
        numero = columna + 1
        coordenada = f"{letra}{numero}"

        x = columna * tam_casilla + 8
        y = fila * tam_casilla + 25

        cv2.putText(
            tablero_transformado,
            coordenada,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# ==========================================
# 9. GUARDAR RESULTADO
# ==========================================
cv2.imwrite(
    "resultados/homografia/tablero_homografia_alternativa.jpg",
    tablero_transformado
)

print("\nImagen guardada: tablero_homografia_alternativa.jpg")