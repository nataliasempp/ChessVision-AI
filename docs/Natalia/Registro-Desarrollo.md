# Registro de desarrollo: asistente inteligente de ajedrez

**Asignatura:** Procesamiento de Imágenes por Computador  
**Proyecto:** Reconocimiento de un tablero físico, cálculo de jugadas con Stockfish y asistencia visual y por voz  
**Sistema operativo:** Ubuntu  

> **Criterio de documentación:** se incluyen los comandos usados durante la preparación y las salidas reales que has compartido. Cuando no has enviado la salida de un comando, se indica expresamente. No se inventan resultados.

## 1. Preparación del proyecto

### 1.1. Instalación de herramientas del sistema

Comando indicado:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

### 1.2. Descarga del repositorio

Comandos indicados:

```bash
git clone https://github.com/alpkirisci/chess_detection_computer_vision.git
cd chess_detection_computer_vision
```

### 1.3. Creación del entorno virtual

Comandos indicados:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Instalación de dependencias de Python

Comandos indicados:

```bash
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python numpy matplotlib pyyaml
```

## 3. Comprobación de los modelos preentrenados

Comando ejecutado:

```bash
ls -lh models/
```

**Salida real:**

```text
total 112M
-rw-rw-r-- 1 natalia natalia 6,0M nov  7 09:36 chess_corner_model.pt
-rw-rw-r-- 1 natalia natalia  50M nov  7 09:36 chess_pieces_model.pt
-rw-rw-r-- 1 natalia natalia 6,0M nov  7 09:36 corner_best.pt
-rw-rw-r-- 1 natalia natalia  50M nov  7 09:36 piece_best.pt
```

**Interpretación:** están disponibles los pesos `corner_best.pt` (detección de esquinas) y `piece_best.pt` (detección de piezas), además de otros dos archivos de modelos. 

## 4. Primera ejecución del detector

Comando ejecutado:

```bash
python chess_inference_example.py
```

**Salida real, inicio y detección de esquinas:**

```text
Creating new Ultralytics Settings v0.0.8 file ✅
View Ultralytics Settings with 'yolo settings' or at '/home/natalia/.config/Ultralytics/settings.json'
Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/usage/settings
🔍 Chess Detection with Dual Model System
==================================================

image 1/1 /home/natalia/Documentos/UC3M/Asignaturas/Procesamiento de IMG/Trabajo final/ChessGame/chess_detection_computer_vision/chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 86.4ms
Speed: 5.1ms preprocess, 86.4ms inference, 3.1ms postprocess per image at shape (1, 3, 640, 640)
✅ Corner model: using 4 corners (reproj err ~ 0.00px)
```

**Salida real, detección de piezas:**

```text
image 1/1 /home/natalia/Documentos/UC3M/Asignaturas/Procesamiento de IMG/Trabajo final/ChessGame/chess_detection_computer_vision/chess_board_image.jpg: 832x832 5 white-pawns, 1 white-rook, 1 white-knight, 1 white-king, 3 black-pawns, 1 black-rook, 1 black-bishop, 1 black-king, 685.6ms
Speed: 3.3ms preprocess, 685.6ms inference, 1.8ms postprocess per image at shape (1, 3, 832, 832)
\nDetection Method: model_detection
Accuracy Level: high
Pieces Detected: 14
```

**Salida real, estado del tablero reconocido:**

```json
{
  "board_state": [
    {"position": "d6", "piece": "white_pawn", "confidence": 0.9601688981056213, "iou": 0.25144887223751367},
    {"position": "b4", "piece": "white_rook", "confidence": 0.9592676162719727, "iou": 0.31071456524295477},
    {"position": "d3", "piece": "black_bishop", "confidence": 0.9571942090988159, "iou": 0.33278739178801625},
    {"position": "e5", "piece": "white_pawn", "confidence": 0.9557639360427856, "iou": 0.2524138853543412},
    {"position": "f4", "piece": "white_knight", "confidence": 0.9540773630142212, "iou": 0.364837746739039},
    {"position": "f2", "piece": "black_rook", "confidence": 0.9538040161132812, "iou": 0.31156065670414496},
    {"position": "d1", "piece": "white_pawn", "confidence": 0.9515189528465271, "iou": 0.2193053370286266},
    {"position": "e1", "piece": "white_king", "confidence": 0.9511099457740784, "iou": 0.5300173558167087},
    {"position": "c7", "piece": "white_pawn", "confidence": 0.9493279457092285, "iou": 0.2555898748653999},
    {"position": "b8", "piece": "white_pawn", "confidence": 0.9489904642105103, "iou": 0.262993075981674},
    {"position": "e8", "piece": "black_pawn", "confidence": 0.9484272003173828, "iou": 0.2855581249769087},
    {"position": "g1", "piece": "black_pawn", "confidence": 0.9474982023239136, "iou": 0.21574281286004446},
    {"position": "f7", "piece": "black_pawn", "confidence": 0.9441943764686584, "iou": 0.2730354778707801},
    {"position": "e6", "piece": "black_king", "confidence": 0.9402931332588196, "iou": 0.6359474778962467}
  ]
}
```

**Salida real, guardado y finalización:**

```text
image 1/1 /home/natalia/Documentos/UC3M/Asignaturas/Procesamiento de IMG/Trabajo final/ChessGame/chess_detection_computer_vision/chess_board_image.jpg: 832x832 5 white-pawns, 1 white-rook, 1 white-knight, 1 white-king, 3 black-pawns, 1 black-rook, 1 black-bishop, 1 black-king, 665.5ms
Speed: 3.7ms preprocess, 665.5ms inference, 1.4ms postprocess per image at shape (1, 3, 832, 832)
Annotated image saved to: annotated_chess_board.jpg
\n✅ Detection completed successfully!
```

### 4.1. Resumen de los resultados

| Pieza reconocida | Cantidad |
|---|---:|
| Peón blanco | 5 |
| Torre blanca | 1 |
| Caballo blanco | 1 |
| Rey blanco | 1 |
| Peón negro | 3 |
| Torre negra | 1 |
| Alfil negro | 1 |
| Rey negro | 1 |
| **Total** | **14** |

Se completó la ejecución y se creó `annotated_chess_board.jpg`. **Todavía no está verificado** que las 14 detecciones y las casillas sean correctas respecto de la imagen original. El texto `Accuracy Level: high` es una salida del programa, no una medida de exactitud calculada frente a anotaciones reales.

## 5. Comprobación visual del reconocimiento de piezas

### 5.1. Visualización de la imagen generada

Después de ejecutar el detector, se ha abierto la imagen anotada para comprobar visualmente los resultados.

**Comando ejecutado:**

```bash
xdg-open annotated_chess_board.jpg
```

**Resultado obtenido:**

Se ha abierto correctamente el archivo `annotated_chess_board.jpg` mediante el visor de imágenes de Ubuntu.

![alt text](../annotated_chess_board.jpg)

La imagen tiene una resolución de 3024 × 3024 píxeles y contiene las detecciones realizadas por YOLO sobre un tablero de ajedrez físico.

El programa representa las piezas mediante cajas delimitadoras de distintos colores. Cada detección incluye:

- Tipo de pieza.
- Color de la pieza.
- Valor de confianza del modelo.
- Localización mediante una caja delimitadora.

### 5.2. Análisis visual de las detecciones

Se ha comprobado que el sistema ha generado 14 detecciones sobre el tablero.

Las cajas delimitadoras se encuentran situadas sobre las piezas y las etiquetas permiten distinguir los tipos identificados.

**Observaciones:**

1. El modelo identifica piezas blancas y negras.
2. Se reconocen diferentes tipos de piezas, entre ellas peones, torres, un caballo, un alfil y reyes.
3. Los valores de confianza de las detecciones se encuentran aproximadamente entre 0,94 y 0,96.
4. Las piezas aparecen detectadas a pesar de que la fotografía está tomada desde una perspectiva inclinada.
5. Se observan varias piezas fuera del tablero que no aparecen incluidas en las detecciones representadas.
6. Algunas etiquetas se superponen, dificultando la inspección visual de determinadas piezas.

La comprobación visual preliminar muestra que el sistema es capaz de localizar e identificar piezas de ajedrez en la imagen de ejemplo.

Sin embargo, todavía no se ha realizado una validación individual de todas las clases y coordenadas predichas frente a una referencia manual.

### 5.3. Conclusiones de la primera prueba

La ejecución del sistema de reconocimiento ha finalizado correctamente y se ha obtenido una imagen con las detecciones realizadas.

Además, el programa ha generado una estructura de datos que relaciona las piezas reconocidas con las coordenadas de las casillas.

Por tanto, se dispone de una primera implementación funcional sobre la imagen de ejemplo del repositorio.

No obstante, para integrar el sistema con un motor de ajedrez será necesario verificar que las posiciones asignadas a las piezas son correctas.

Un error en la identificación de una pieza o en su casilla podría provocar que el motor analizase una posición diferente de la real.


## 6. Reconstrucción digital del tablero

### 6.1. Instalación de python-chess

Una vez comprobado el funcionamiento inicial del detector YOLO, se ha comenzado a preparar la reconstrucción digital del tablero.

Para ello, se utilizará la biblioteca `python-chess`, que permite representar posiciones de ajedrez, gestionar los movimientos y comprobar su legalidad.

**Comando ejecutado:**

```bash
python -m pip install python-chess
```

**Salida real obtenida (resumen):**

```text
Collecting python-chess
Collecting chess<2,>=1 (from python-chess)
Successfully built chess
Installing collected packages: chess, python-chess
Successfully installed chess-1.11.2 python-chess-1.999
```

La instalación se ha realizado correctamente dentro del entorno virtual `.venv`.

### 6.2. Comprobación de la instalación

Para verificar que Python reconoce la biblioteca, se ha ejecutado:

```bash
python -c "import chess; print('python-chess instalado correctamente')"
```

**Salida real:**

```text
python-chess instalado correctamente
```

**Resultado:**

Se ha comprobado que la biblioteca está correctamente instalada y puede importarse desde Python.

Con ello, el entorno está preparado para comenzar a transformar las detecciones obtenidas mediante YOLO en una representación digital del tablero.

### 6.3. Primera reconstrucción digital del tablero

Una vez instalada la biblioteca `python-chess`, se ha desarrollado un primer programa para representar digitalmente las piezas detectadas por YOLO.

Para ello, se ha creado el archivo:

```text
reconstruir_tablero.py
```

El programa utiliza las 14 detecciones obtenidas durante la primera ejecución de YOLO. Cada detección contiene el tipo de pieza y la casilla asignada.

En esta primera prueba, las detecciones se han introducido manualmente a partir de la salida del detector. La integración automática queda pendiente.

El programa realiza las siguientes operaciones:

1. Crea un tablero vacío mediante `chess.Board(None)`.
2. Convierte las clases detectadas por YOLO a símbolos de ajedrez.
3. Coloca cada pieza en su casilla mediante `set_piece_at()`.
4. Muestra el tablero reconstruido.
5. Genera la representación FEN.
6. Comprueba el número de piezas y la validez de la posición.

**Comando ejecutado:**

```bash
python reconstruir_tablero.py
```

**Salida real obtenida:**

```text
TABLERO RECONSTRUIDO:

. P . . p . . .
. . P . . p . .
. . . P k . . .
. . . . P . . .
. R . . . N . .
. . . b . . . .
. . . . . r . .
. . . P K . p .

POSICIÓN FEN:
1P2p3/2P2p2/3Pk3/4P3/1R3N2/3b4/5r2/3PK1p1 w - - 0 1

NÚMERO DE PIEZAS:
14

¿ES UNA POSICIÓN VÁLIDA?
False
```

### 6.4. Análisis de los resultados

Se ha conseguido representar las 14 detecciones mediante un tablero digital de 8 × 8.

El número de piezas reconstruidas coincide con el número de detecciones proporcionadas por YOLO.

También se ha generado una cadena FEN, que permite representar la posición de las piezas en un formato compatible con motores de ajedrez.

Sin embargo, la comprobación de validez ha devuelto:

```text
False
```

Al analizar las coordenadas detectadas, se observa que existen peones situados en la primera y octava fila:

| Pieza | Casilla |
|---|---|
| Peón blanco | b8 |
| Peón blanco | d1 |
| Peón negro | e8 |
| Peón negro | g1 |

Estas posiciones no son válidas en una partida de ajedrez, ya que los peones deben promocionar al alcanzar la última fila.

Por tanto, aunque la reconstrucción digital funciona, todavía no se puede garantizar que las coordenadas asignadas por el sistema de visión sean correctas.

Además, el FEN generado utiliza por defecto el turno de las blancas y no incorpora información histórica sobre enroques o capturas al paso.

### 6.5. Conclusiones

La primera reconstrucción digital se ha ejecutado correctamente y ha permitido obtener un tablero con las piezas detectadas por YOLO.

Se ha identificado una limitación importante: las coordenadas proporcionadas por el sistema de reconocimiento pueden generar posiciones incompatibles con las reglas del ajedrez.

Esto demuestra la necesidad de incorporar una fase de validación entre el reconocimiento visual y el análisis de jugadas.

Antes de integrar Stockfish será necesario comprobar la orientación del tablero y la correspondencia entre las casillas detectadas y las posiciones reales de las piezas.

**Estado:** reconstrucción digital implementada. Validación de coordenadas pendiente.

### 6.6. Diagnóstico de los errores de validez

Después de comprobar que el tablero reconstruido no era válido, se ha ampliado el programa `reconstruir_tablero.py` para identificar las condiciones que provocan este resultado.

Para ello, se ha utilizado el método `status()` de la biblioteca `python-chess`.

**Código añadido:**

```python
# ==========================================
# 6. DIAGNÓSTICO DE LA POSICIÓN
# ==========================================

print("\nDIAGNÓSTICO DE LA POSICIÓN:")

estado = tablero.status()

print("Código de estado:", estado)

for nombre in dir(chess):
    if nombre.startswith("STATUS_"):
        valor = getattr(chess, nombre)

        if valor != chess.STATUS_VALID and estado & valor:
            print("Problema detectado:", nombre)
```

**Comando ejecutado:**

```bash
python reconstruir_tablero.py
```

**Salida real obtenida:**

```text
DIAGNÓSTICO DE LA POSICIÓN:
Código de estado: Status.OPPOSITE_CHECK|PAWNS_ON_BACKRANK
Problema detectado: STATUS_OPPOSITE_CHECK
Problema detectado: STATUS_PAWNS_ON_BACKRANK
```

### 6.7. Análisis de los errores detectados

El diagnóstico ha identificado dos problemas.

**1. STATUS_PAWNS_ON_BACKRANK**

Indica que existen peones situados en la primera u octava fila.

En la reconstrucción se han identificado las siguientes posiciones:

| Pieza | Casilla |
|---|---|
| Peón blanco | b8 |
| Peón blanco | d1 |
| Peón negro | e8 |
| Peón negro | g1 |

Estas posiciones no corresponden a un estado legal del juego, ya que los peones deben promocionar cuando alcanzan la última fila.

**2. STATUS_OPPOSITE_CHECK**

Indica que el jugador al que no le corresponde mover se encuentra en jaque.

En el FEN generado, el turno se ha establecido por defecto para las blancas.

Sin embargo, el rey negro situado en `e6` está atacado por el peón blanco situado en `d6`.

Esto produce una incompatibilidad entre el turno asignado y la disposición de las piezas.

### 6.8. Conclusiones

El diagnóstico confirma que la reconstrucción digital contiene una posición incompatible con las reglas del ajedrez.

Se han identificado dos posibles fuentes de error:

1. Asignación incorrecta de coordenadas o clases a determinadas piezas.
2. Falta de información sobre el turno de juego.

Antes de integrar Stockfish, será necesario comprobar visualmente las posiciones detectadas y determinar correctamente la orientación del tablero.

Esta prueba demuestra que la validación mediante `python-chess` puede utilizarse como una etapa adicional para detectar inconsistencias en las salidas del sistema de visión.

**Estado:** diagnóstico implementado. Corrección de las posiciones pendiente.

### 6.9. Localización de las funciones de asignación de casillas

Tras detectar que la posición reconstruida contiene inconsistencias, se ha comenzado a analizar el funcionamiento interno del programa `chess_inference_example.py`.

El objetivo es identificar cómo se transforma la posición de las piezas detectadas en la imagen a coordenadas del tablero de ajedrez.

**Comando ejecutado:**

```bash
grep -nE "def |homography|perspective|square|board_state" chess_inference_example.py
```

**Salida real obtenida:**

```text
5:Now uses a robust, corner-based perspective mapping (homography) so pieces
6:are assigned to the correct squares even when the board is tilted or only
17:def warp_pts(H, pts_xy):
19:    return cv2.perspectiveTransform(pts, H).reshape(-1, 2)
21:def best_H_for_4points(pts4, warp_size=800):
35:        raise ValueError("No valid homography for given 4 points")
38:def cluster_points(points, confs, tol=150.0):
54:def select_best_4(points, warp_size=800):
70:def extract_raw_corner_centers(corner_model: YOLO, image_path: str, conf_threshold=0.25):
85:def grid_squares(warp_size=800):
86:    squares = {}
93:            squares[pos] = [x1, y1, x2, y2]
94:    return squares
96:def rect_iou(a, b):
107:def map_box_to_square_via_bottom_strip(x1, y1, x2, y2, H, squares, warp_size=800, strip_frac=0.25):
119:    for pos, sq in squares.items():
134:def detect_chess_pieces(model_path, image_path, corner_model_path=None, conf_threshold=0.25, warp_size=800):
155:    # Determine board homography H
160:    # Compute homography from detected corners (required)
179:    board_state = []
180:    squares = grid_squares(warp_size=warp_size) if H is not None else None
191:                # Skip empty squares
195:                # Map to board square
196:                pos, iou = map_box_to_square_via_bottom_strip(x1, y1, x2, y2, H, squares, warp_size=warp_size, strip_frac=0.25)
201:                board_state.append({
208:    # Keep only the highest-confidence detection per square
210:    for det in board_state:
214:    board_state = list(dedup.values())
217:        "board_state": board_state,
225:def visualize_detections(model_path, image_path, output_path=None):
266:        print(f"Pieces Detected: {len(result['board_state'])}")
269:        print(json.dumps({"board_state": result["board_state"]}, indent=2))
```

**Análisis preliminar:**

Se ha identificado que el programa utiliza una transformación de perspectiva basada en homografía para relacionar las posiciones de la imagen con las casillas del tablero.

También se han localizado las funciones encargadas de crear la cuadrícula de 8 × 8 y asignar las detecciones a sus correspondientes casillas.

Las funciones principales que se revisarán son `best_H_for_4points()`, `grid_squares()` y `map_box_to_square_via_bottom_strip()`.

**Estado:** funciones identificadas. Análisis de su implementación pendiente.

### 6.10. Análisis del código de transformación de perspectiva

Para investigar los errores detectados en las coordenadas del tablero, se ha revisado la implementación de las funciones de transformación de perspectiva y asignación de casillas.

**Comando ejecutado:**

```bash
sed -n '1,135p' chess_inference_example.py
```

El comando ha permitido consultar las funciones encargadas de detectar y seleccionar las esquinas, calcular la homografía y determinar la casilla correspondiente a cada pieza.

**Funciones analizadas:**

- `best_H_for_4points()`: calcula una homografía a partir de cuatro puntos.
- `select_best_4()`: selecciona una combinación de cuatro puntos detectados.
- `extract_raw_corner_centers()`: obtiene los centros de las cajas delimitadoras correspondientes a las esquinas.
- `grid_squares()`: genera una cuadrícula de 8 × 8 y asigna coordenadas a las 64 casillas.
- `map_box_to_square_via_bottom_strip()`: transforma la región inferior de cada caja delimitadora y selecciona la casilla con mayor solapamiento.

**Observaciones:**

Se ha identificado que el programa prueba diferentes permutaciones de las cuatro esquinas y selecciona la que presenta menor error de reproyección.

Sin embargo, un error de reproyección reducido no garantiza que las esquinas estén ordenadas de acuerdo con la orientación real del tablero.

También se ha observado que la función de extracción de esquinas utiliza sus coordenadas y confianzas, pero no las clases predichas por YOLO para establecer su orientación.

Por otro lado, la asignación de piezas utiliza el 25 % inferior de cada caja delimitadora, que se transforma mediante la homografía y se compara con las casillas de la cuadrícula.

**Conclusión preliminar:**

Se ha identificado una posible limitación en el procedimiento de selección y ordenación de esquinas.

Una orientación incorrecta podría provocar errores en las coordenadas asignadas a las piezas, incluso cuando estas han sido detectadas correctamente.

No obstante, todavía es necesario revisar el resto de la implementación y comprobar visualmente la transformación antes de confirmar el origen del problema.

**Estado:** análisis preliminar realizado. Validación de la homografía pendiente.

### 6.11. Revisión del procedimiento de asignación de piezas

Para completar el análisis de la reconstrucción digital, se ha revisado la función principal `detect_chess_pieces()` del archivo `chess_inference_example.py`.

**Comando ejecutado:**

```bash
sed -n '134,225p' chess_inference_example.py
```

**Resultado:**

Se ha comprobado que el programa realiza las siguientes operaciones:

1. Carga los modelos YOLO de detección de esquinas y piezas.
2. Detecta las esquinas y agrupa las detecciones cercanas.
3. Selecciona cuatro puntos para calcular la homografía.
4. Detecta las piezas presentes en la imagen.
5. Transforma sus posiciones mediante la homografía.
6. Asigna cada pieza a la casilla con mayor solapamiento.
7. Elimina las detecciones duplicadas que se hayan asignado a una misma casilla.

**Observaciones:**

El código utiliza una transformación de perspectiva para relacionar las coordenadas de la imagen original con las casillas de un tablero de 800 × 800 píxeles.

Sin embargo, no se ha identificado una comprobación explícita de que la orientación del tablero transformado coincida con la orientación utilizada para asignar las coordenadas algebraicas.

Asimismo, se ha observado que, cuando varias detecciones se asignan a una misma casilla, únicamente se conserva aquella con mayor confianza.

Estas características podrían influir en la reconstrucción de la posición.

**Conclusión:**

Se considera necesario visualizar el resultado de la homografía para comprobar si las cuatro esquinas seleccionadas corresponden al tablero y si la cuadrícula transformada coincide con las casillas reales.

Como siguiente prueba, se propone crear un programa independiente que genere una imagen del tablero transformado y superponga una cuadrícula de 8 × 8.

**Estado:** código revisado. Visualización de la homografía pendiente.

### 6.12. Validación visual de la transformación de perspectiva

Para comprobar si los errores de asignación de casillas se deben a la transformación de perspectiva, se ha creado el archivo `visualizar_homografia.py`.

Este programa utiliza las funciones del detector original para obtener la homografía y transformar la fotografía del tablero en una imagen de 800 × 800 píxeles.

Sobre el resultado se ha dibujado una cuadrícula verde de 8 × 8 para comprobar su correspondencia con las casillas reales.

**Comando ejecutado:**

```bash
python visualizar_homografia.py
```

**Salida real obtenida:**

```text
image 1/1 .../chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 114.0ms
Speed: 3.7ms preprocess, 114.0ms inference, 1.7ms postprocess per image at shape (1, 3, 640, 640)

ESQUINAS DETECTADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ESQUINAS TRAS AGRUPACIÓN:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ERROR DE REPROYECCIÓN:
0.0

PERMUTACIÓN SELECCIONADA:
(2, 1, 0, 3)

ESQUINAS UTILIZADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

Imagen guardada: tablero_homografia.jpg
```

**Visualización del resultado:**

```bash
xdg-open tablero_homografia.jpg
```

Se ha obtenido una imagen de 800 × 800 píxeles que muestra el tablero transformado y una cuadrícula superpuesta.

![alt text](../tablero_homografia.jpg)

**Análisis de los resultados:**

La inspección visual muestra que la cuadrícula generada coincide aproximadamente con los límites de las casillas del tablero físico.

Esto indica que la transformación de perspectiva funciona correctamente desde el punto de vista geométrico para la imagen analizada.

Sin embargo, el programa selecciona la permutación de esquinas que minimiza el error de reproyección, sin comprobar explícitamente que la orientación obtenida coincida con las coordenadas algebraicas del tablero.

Por tanto, aunque la transformación geométrica parece adecuada, todavía no se puede garantizar que las coordenadas asignadas a las piezas correspondan a las casillas reales.

Conclusión:

La prueba permite comprobar que el tablero se transforma correctamente a una vista prácticamente cenital.

El siguiente paso será superponer las coordenadas algebraicas sobre la imagen transformada para comprobar su orientación y determinar si existe algún error en la correspondencia entre las casillas físicas y las digitales.

Estado: transformación de perspectiva comprobada visualmente. Orientación de coordenadas pendiente de validación.

### 6.12. Validación visual de la transformación de perspectiva

Para comprobar si los errores de asignación de casillas se deben a la transformación de perspectiva, se ha creado el archivo `visualizar_homografia.py`.

Este programa utiliza las funciones del detector original para obtener la homografía y transformar la fotografía del tablero en una imagen de 800 × 800 píxeles.

Sobre el resultado se ha dibujado una cuadrícula verde de 8 × 8 para comprobar su correspondencia con las casillas reales.

**Comando ejecutado:**

```bash
python visualizar_homografia.py
```

**Salida real obtenida:**

```text
image 1/1 .../chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 114.0ms
Speed: 3.7ms preprocess, 114.0ms inference, 1.7ms postprocess per image at shape (1, 3, 640, 640)

ESQUINAS DETECTADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ESQUINAS TRAS AGRUPACIÓN:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ERROR DE REPROYECCIÓN:
0.0

PERMUTACIÓN SELECCIONADA:
(2, 1, 0, 3)

ESQUINAS UTILIZADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

Imagen guardada: tablero_homografia.jpg
```

**Visualización del resultado:**

```bash
xdg-open tablero_homografia.jpg
```

Se ha obtenido una imagen de 800 × 800 píxeles que muestra el tablero transformado y una cuadrícula superpuesta.

**Análisis de los resultados:**

La inspección visual muestra que la cuadrícula generada coincide aproximadamente con los límites de las casillas del tablero físico.

Esto indica que la transformación de perspectiva funciona correctamente desde el punto de vista geométrico para la imagen analizada.

Sin embargo, el programa selecciona la permutación de esquinas que minimiza el error de reproyección, sin comprobar explícitamente que la orientación obtenida coincida con las coordenadas algebraicas del tablero.

Por tanto, aunque la transformación geométrica parece adecuada, todavía no se puede garantizar que las coordenadas asignadas a las piezas correspondan a las casillas reales.

**Conclusión:**

La prueba permite comprobar que el tablero se transforma correctamente a una vista prácticamente cenital.

El siguiente paso será superponer las coordenadas algebraicas sobre la imagen transformada para comprobar su orientación y determinar si existe algún error en la correspondencia entre las casillas físicas y las digitales.

**Estado:** transformación de perspectiva comprobada visualmente. Orientación de coordenadas pendiente de validación.

### 6.13. Comprobación de la orientación de las coordenadas

Una vez validada visualmente la transformación de perspectiva, se ha realizado una nueva prueba para comprobar la correspondencia entre las casillas del tablero físico y las coordenadas algebraicas utilizadas por el programa.

Para ello, se ha modificado el archivo `visualizar_homografia.py` añadiendo las coordenadas de las 64 casillas sobre la imagen transformada.

**Código añadido:**

```python
for fila in range(8):
    for columna in range(8):

        letra = chr(ord("a") + columna)
        numero = 8 - fila

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
```

**Comando ejecutado:**

```bash
python visualizar_homografia.py
```

**Salida real obtenida:**

```text
image 1/1 .../chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 52.3ms
Speed: 3.0ms preprocess, 52.3ms inference, 0.8ms postprocess per image at shape (1, 3, 640, 640)

ESQUINAS DETECTADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ESQUINAS TRAS AGRUPACIÓN:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ERROR DE REPROYECCIÓN:
0.0

PERMUTACIÓN SELECCIONADA:
(2, 1, 0, 3)

ESQUINAS UTILIZADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

Imagen guardada: tablero_homografia.jpg
```

**Comando utilizado para visualizar el resultado:**

```bash
xdg-open tablero_homografia.jpg
```

**Imagen obtenida:**

![Tablero transformado con coordenadas](../tablero_homografia.jpg)

### Análisis de los resultados

La imagen obtenida muestra el tablero transformado a una vista prácticamente cenital, con una cuadrícula verde de 8 × 8 y las coordenadas algebraicas representadas en rojo.

Se observa que las líneas de la cuadrícula coinciden aproximadamente con los límites reales de las casillas, lo que confirma visualmente que la transformación de perspectiva funciona de manera adecuada para esta fotografía.

Sin embargo, se ha identificado un posible problema en la orientación de las coordenadas.

El programa asigna la coordenada `a8` a la casilla superior izquierda de la imagen transformada. Esta casilla es oscura, mientras que en un tablero de ajedrez correctamente orientado la casilla `a8` debe ser clara.

Por tanto, la orientación de las coordenadas generadas no es compatible con la disposición convencional de los colores del tablero.

Esta observación podría explicar parte de las inconsistencias encontradas anteriormente, como la presencia de peones en la primera y octava fila.

No obstante, todavía es necesario comparar las coordenadas con las letras y números impresos en el tablero físico antes de determinar la orientación correcta.

### Conclusiones

Se ha comprobado que la transformación geométrica permite obtener una representación cenital adecuada del tablero.

También se ha identificado una posible inconsistencia en la orientación de las coordenadas algebraicas.

Como siguiente paso, se propone probar una orientación alternativa de las coordenadas y comparar visualmente el resultado con el tablero físico.

**Estado:** transformación de perspectiva validada visualmente. Posible error de orientación identificado. Corrección pendiente.

### 6.14. Prueba de una orientación alternativa de las coordenadas

Tras identificar una posible inconsistencia en la orientación de las coordenadas, se ha realizado una segunda prueba modificando únicamente la forma de asignar los nombres de las casillas.

El objetivo es comprobar si una orientación alternativa resulta más coherente con la disposición del tablero físico.

**Código modificado en `visualizar_homografia.py`:**

Orientación original:

```python
letra = chr(ord("a") + columna)
numero = 8 - fila
```

Orientación alternativa:

```python
letra = chr(ord("a") + fila)
numero = columna + 1
```

Con esta modificación, la primera fila de la imagen transformada pasa a contener las coordenadas:

```text
a1  a2  a3  a4  a5  a6  a7  a8
```

**Comando ejecutado:**

```bash
python visualizar_homografia.py
```

**Salida real obtenida:**

```text
image 1/1 .../chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 100.6ms

Speed: 2.6ms preprocess, 100.6ms inference, 0.8ms postprocess per image at shape (1, 3, 640, 640)

ESQUINAS DETECTADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ESQUINAS TRAS AGRUPACIÓN:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

ERROR DE REPROYECCIÓN:
0.0

PERMUTACIÓN SELECCIONADA:
(2, 1, 0, 3)

ESQUINAS UTILIZADAS:
[[2322.1 1904.5]
 [1764.9 974.68]
 [612.12 1251.4]
 [914.31 2344.7]]

Imagen guardada: tablero_homografia.jpg
```

**Comando utilizado para visualizar la orientación alternativa:**

```bash
xdg-open tablero_homografia_alternativa.jpg
```

**Imagen obtenida:**

![Tablero con coordenadas alternativas](../tablero_homografia_alternativa.jpg)

### Análisis de los resultados

La nueva imagen mantiene la misma transformación de perspectiva y cuadrícula de 8 × 8, pero modifica la orientación de las coordenadas algebraicas.

Se observa que la casilla superior izquierda pasa a identificarse como `a1`, que es una casilla oscura, y la superior derecha como `a8`, que es una casilla clara.

Esta distribución resulta coherente con los colores convencionales de dichas coordenadas.

Además, al considerar esta orientación alternativa, los peones que anteriormente aparecían en las filas extremas pasarían a ocupar casillas interiores.

Por ejemplo:

| Posición original | Posición alternativa |
|---|---|
| b8 | a2 |
| d1 | h4 |
| e8 | a5 |
| g1 | h7 |

Esto sugiere que la orientación de las coordenadas podría ser una de las causas de las inconsistencias detectadas en la reconstrucción digital.

Sin embargo, la correspondencia exacta con las coordenadas impresas en el tablero físico todavía no se ha verificado.

También queda pendiente comprobar el nombre del archivo generado, ya que la salida de la terminal sigue indicando `tablero_homografia.jpg`.

### Conclusiones

La orientación alternativa presenta una distribución de colores coherente con las coordenadas del ajedrez y podría resolver parte de los errores detectados anteriormente.

No obstante, todavía no se ha modificado la función original de asignación de casillas ni se ha generado un nuevo FEN utilizando esta orientación.

El siguiente paso será verificar la orientación física del tablero y comprobar si la nueva correspondencia permite reconstruir una posición válida mediante `python-chess`.

**Estado:** orientación alternativa visualizada. Validación definitiva pendiente.

### 6.15. Corrección de la orientación del tablero

Tras comprobar las coordenadas impresas en el tablero físico, se ha confirmado que la orientación utilizada inicialmente por el detector era incorrecta.

Para solucionar este problema, se ha modificado la función `grid_squares()` del archivo `chess_inference_example.py`.

**Código original:**

```python
pos = chr(ord('a') + c) + str(8 - r)
```

**Código modificado:**

```python
pos = chr(ord('a') + r) + str(c + 1)
```

Esta modificación permite adaptar la asignación de coordenadas a la orientación real del tablero de la fotografía.

No ha sido necesario modificar los modelos YOLO ni el procedimiento de transformación de perspectiva.

**Comando ejecutado:**

```bash
python chess_inference_example.py
```

**Salida real obtenida (resumen):**

```text
image 1/1 .../chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 118.0ms

Corner model: using 4 corners (reproj err ~ 0.00px)

image 1/1 .../chess_board_image.jpg: 832x832 5 white-pawns, 1 white-rook, 1 white-knight, 1 white-king, 3 black-pawns, 1 black-rook, 1 black-bishop, 1 black-king, 517.0ms

Detection Method: model_detection
Accuracy Level: high
Pieces Detected: 14

Annotated image saved to: annotated_chess_board.jpg

Detection completed successfully!
```

**Nuevas coordenadas obtenidas:**

| Pieza detectada | Casilla | Confianza |
|---|---|---:|
| Peón blanco | c4 | 0,960 |
| Torre blanca | e2 | 0,959 |
| Alfil negro | f4 | 0,957 |
| Peón blanco | d5 | 0,956 |
| Caballo blanco | e6 | 0,954 |
| Torre negra | g6 | 0,954 |
| Peón blanco | h4 | 0,952 |
| Rey blanco | h5 | 0,951 |
| Peón blanco | b3 | 0,949 |
| Peón blanco | a2 | 0,949 |
| Peón negro | a5 | 0,948 |
| Peón negro | h7 | 0,947 |
| Peón negro | b6 | 0,944 |
| Rey negro | c5 | 0,940 |

**Análisis de los resultados:**

La ejecución ha vuelto a detectar las 14 piezas, manteniendo sus clases y valores de confianza.

La modificación ha cambiado únicamente las coordenadas asignadas a las piezas.

Se observa que los cuatro peones que anteriormente aparecían en las filas extremas han pasado a ocupar casillas interiores.

Esto indica que el problema de los peones en la primera y octava fila estaba relacionado con la orientación utilizada para asignar las coordenadas.

**Conclusión:**

Se ha corregido la orientación de las coordenadas del tablero, consiguiendo una correspondencia con las referencias impresas en el tablero físico.

La modificación soluciona el problema identificado de los peones en las filas extremas sin necesidad de volver a entrenar los modelos.

Como siguiente paso, se comprobará la validez de la nueva posición mediante `python-chess`.

**Estado:** orientación corregida. Validación de la nueva posición pendiente.

### 6.16. Validación de la posición tras corregir la orientación

Después de modificar la función de asignación de coordenadas, se ha actualizado el archivo `reconstruir_tablero.py` con las nuevas posiciones obtenidas mediante YOLO.

El objetivo es comprobar si la corrección permite reconstruir una posición válida.

**Comando ejecutado:**

```bash
python reconstruir_tablero.py
```

**Salida real obtenida:**

```text
TABLERO RECONSTRUIDO:

. . . . . . . .
. . . . . . . p
. p . . N . r .
p . k P . . . K
. . P . . b . P
. P . . . . . .
P . . . R . . .
. . . . . . . .

POSICIÓN FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 w - - 0 1

NÚMERO DE PIEZAS:
14

¿ES UNA POSICIÓN VÁLIDA?
False

DIAGNÓSTICO DE LA POSICIÓN:
Código de estado: Status.OPPOSITE_CHECK
Problema detectado: STATUS_OPPOSITE_CHECK
```

**Análisis de los resultados:**

La reconstrucción contiene las 14 piezas detectadas por YOLO.

Tras corregir la orientación, ha desaparecido el error `STATUS_PAWNS_ON_BACKRANK`, que indicaba la presencia de peones en la primera u octava fila.

Esto confirma que el problema estaba relacionado con la asignación inicial de coordenadas.

Sin embargo, continúa apareciendo el error `STATUS_OPPOSITE_CHECK`.

En la posición reconstruida, el rey negro se encuentra en `c5` y está atacado por el caballo blanco situado en `e6`.

El FEN generado establece por defecto el turno de las blancas, lo que resulta incompatible con que el rey negro se encuentre en jaque.

**Conclusión:**

La corrección de orientación ha solucionado uno de los dos problemas de validez detectados inicialmente.

La posición sigue siendo inválida debido a la relación entre el turno asignado y las amenazas existentes sobre el tablero.

Como siguiente paso, se comprobará si asignar el turno a las negras permite obtener una posición válida.

**Estado:** error de orientación corregido. Validación del turno pendiente.

### 6.17. Validación del tablero mediante el cambio de turno

Tras corregir la orientación de las coordenadas, el tablero reconstruido seguía presentando el error `STATUS_OPPOSITE_CHECK`.

Este error se debía a que el rey negro se encontraba amenazado mientras que el turno estaba asignado a las blancas.

Para comprobar si el problema estaba relacionado con el turno, se ha modificado el archivo `reconstruir_tablero.py`.

**Código añadido:**

```python
tablero.turn = chess.BLACK
```

Esta instrucción establece el turno de las negras.

**Comando ejecutado:**

```bash
python reconstruir_tablero.py
```

**Salida real obtenida:**

```text
TABLERO RECONSTRUIDO:

. . . . . . . .
. . . . . . . p
. p . . N . r .
p . k P . . . K
. . P . . b . P
. P . . . . . .
P . . . R . . .
. . . . . . . .

POSICIÓN FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

NÚMERO DE PIEZAS:
14

¿ES UNA POSICIÓN VÁLIDA?
True

DIAGNÓSTICO DE LA POSICIÓN:
Código de estado: Status.VALID
```

**Análisis de los resultados:**

Al establecer el turno de las negras, la posición reconstruida pasa a considerarse válida por la biblioteca `python-chess`.

El error `STATUS_OPPOSITE_CHECK` desaparece, ya que el rey negro puede encontrarse en jaque cuando corresponde jugar a las negras.

La representación conserva las 14 piezas detectadas y genera correctamente la posición FEN.

Se confirma que la orientación corregida y la asignación adecuada del turno permiten obtener una posición compatible con las comprobaciones de validez de la biblioteca.

Sin embargo, el turno se ha establecido manualmente para realizar esta prueba. Todavía no existe un procedimiento automático para determinarlo a partir de la partida.

**Conclusión:**

Se ha conseguido reconstruir una posición válida mediante `python-chess` a partir de las detecciones de YOLO.

Este resultado permite avanzar hacia la integración con Stockfish, encargado de analizar la posición y recomendar movimientos.

**Estado:** reconstrucción digital validada para la posición de prueba con turno de las negras. Integración con Stockfish pendiente.

## 7. Integración del motor de ajedrez Stockfish

### 7.1. Instalación de Stockfish

Una vez obtenida una posición válida mediante `python-chess`, se ha comenzado la integración del motor de ajedrez Stockfish.

Stockfish permite analizar posiciones de ajedrez y calcular movimientos recomendados. Su incorporación permitirá que el sistema proporcione asistencia al jugador después de reconocer el tablero físico.

Para instalarlo en Ubuntu, se han ejecutado los siguientes comandos:

```bash
sudo apt update
sudo apt install stockfish
```

**Salida real relevante:**

```text
Se instalarán los siguientes paquetes NUEVOS:
  stockfish

Se necesita descargar 24,8 MB de archivos.
Se utilizarán 47,4 MB de espacio de disco adicional después de esta operación.

Desempaquetando stockfish (14.1-1) ...
Configurando stockfish (14.1-1) ...
```

La instalación se ha completado correctamente, utilizando el paquete Stockfish 14.1 disponible en los repositorios de Ubuntu.

### 7.2. Comprobación del funcionamiento

Para comprobar que el motor se ha instalado correctamente, se ha ejecutado:

```bash
/usr/games/stockfish
```

**Salida real:**

```text
Stockfish 14.1 by the Stockfish developers (see AUTHORS file)
```

Para finalizar la ejecución interactiva se ha utilizado:

```text
quit
```

**Resultado:**

Se ha comprobado que Stockfish puede ejecutarse correctamente desde la terminal de Ubuntu.

El siguiente objetivo será utilizar la biblioteca `python-chess` para enviarle la posición reconstruida y obtener una recomendación de movimiento.

**Estado:** Stockfish instalado y comprobado. Integración mediante Python pendiente.

### 7.3. Primera integración de Stockfish con python-chess

Una vez instalado y comprobado el funcionamiento de Stockfish, se ha integrado el motor de ajedrez en el programa `reconstruir_tablero.py`.

El objetivo de esta fase es analizar la posición reconstruida a partir de las detecciones de YOLO y obtener una recomendación de movimiento.

Para ello, se ha utilizado el módulo `chess.engine` de la biblioteca `python-chess`, que permite comunicarse con motores de ajedrez compatibles con el protocolo UCI.

**Código añadido:**

```python
import chess.engine

# ==========================================
# ANÁLISIS CON STOCKFISH
# ==========================================

print("\nANÁLISIS CON STOCKFISH:")

if tablero.is_valid():

    ruta_stockfish = "/usr/games/stockfish"

    motor = chess.engine.SimpleEngine.popen_uci(
        ruta_stockfish
    )

    try:
        resultado = motor.analyse(
            tablero,
            chess.engine.Limit(time=2.0)
        )

        mejor_jugada = resultado["pv"][0]

        print("\nMejor jugada (UCI):")
        print(mejor_jugada.uci())

        print("\nMejor jugada (notación SAN):")
        print(tablero.san(mejor_jugada))

        evaluacion = resultado["score"].white()

        print("\nEvaluación de la posición:")
        print(evaluacion)

    finally:
        motor.quit()

else:
    print("La posición no es válida.")
    print("No se puede realizar el análisis.")
```

**Comando ejecutado:**

```bash
python reconstruir_tablero.py
```

**Salida real obtenida:**

```text
TABLERO RECONSTRUIDO:

. . . . . . . .
. . . . . . . p
. p . . N . r .
p . k P . . . K
. . P . . b . P
. P . . . . . .
P . . . R . . .
. . . . . . . .

POSICIÓN FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

NÚMERO DE PIEZAS:
14

¿ES UNA POSICIÓN VÁLIDA?
True

DIAGNÓSTICO DE LA POSICIÓN:
Código de estado: Status.VALID

ANÁLISIS CON STOCKFISH:

Mejor jugada (UCI):
c5b4

Mejor jugada (notación SAN):
Kb4

Evaluación de la posición:
+940
```

### Análisis de los resultados

La integración se ha ejecutado correctamente y Stockfish ha analizado la posición reconstruida.

El motor ha recomendado el movimiento `c5b4`, correspondiente al desplazamiento del rey negro desde la casilla `c5` hasta `b4`.

La jugada también se ha representado mediante notación algebraica estándar como `Kb4`.

Además, se ha obtenido una evaluación de `+940` centipeones desde el punto de vista de las blancas, equivalente aproximadamente a una ventaja de 9,40 peones.

El análisis se ha realizado utilizando un tiempo de cálculo de dos segundos.

### Conclusiones

Se ha conseguido integrar correctamente python-chess con Stockfish y obtener una recomendación de movimiento a partir de una posición reconstruida mediante las detecciones iniciales de YOLO.

Con ello, se ha comprobado el funcionamiento de los principales componentes del sistema de manera independiente.

Sin embargo, las detecciones todavía se introducen manualmente en el programa de reconstrucción y el turno de juego se establece de forma explícita.

Por tanto, el siguiente objetivo será automatizar la transferencia de información entre el detector YOLO y el módulo de análisis de ajedrez.

Estado: integración de Stockfish implementada y comprobada. Automatización del proceso pendiente.

### 7.4. Automatización del reconocimiento y análisis de jugadas

Una vez comprobado el funcionamiento independiente de YOLO, `python-chess` y Stockfish, se ha desarrollado un programa que integra los tres componentes.

El objetivo es automatizar el proceso completo, desde la detección de las piezas en una fotografía hasta la recomendación de una jugada, sin necesidad de introducir manualmente las detecciones.

Para ello, se ha creado el archivo:

```text
asistente_ajedrez.py
```

Este programa realiza las siguientes operaciones:

1. Carga los modelos YOLO de detección de esquinas y piezas.
2. Procesa la fotografía del tablero.
3. Obtiene automáticamente las piezas detectadas y sus coordenadas.
4. Reconstruye el tablero utilizando `python-chess`.
5. Genera la representación FEN.
6. Comprueba la validez de la posición.
7. Envía la posición a Stockfish.
8. Obtiene la jugada recomendada y la evaluación.

**Código principal de integración:**

```python
resultado = detect_chess_pieces(
    model_path=MODELO_PIEZAS,
    image_path=IMAGEN,
    corner_model_path=MODELO_ESQUINAS
)

detecciones = resultado["board_state"]
```

Esta parte permite utilizar directamente las detecciones proporcionadas por YOLO.

Posteriormente, las piezas se colocan en un tablero digital y se comprueba su validez antes de solicitar el análisis a Stockfish.

**Comando ejecutado:**

```bash
python asistente_ajedrez.py
```

**Salida real obtenida:**

```text
1. DETECTANDO TABLERO Y PIEZAS...

image 1/1 .../chess_board_image.jpg: 640x640 2 top_lefts, 1 top_right, 1 bottom_left, 88.1ms
Speed: 2.6ms preprocess, 88.1ms inference, 2.5ms postprocess per image at shape (1, 3, 640, 640)

Corner model: using 4 corners (reproj err ~ 0.00px)

image 1/1 .../chess_board_image.jpg: 832x832 5 white-pawns, 1 white-rook, 1 white-knight, 1 white-king, 3 black-pawns, 1 black-rook, 1 black-bishop, 1 black-king, 453.7ms
Speed: 5.7ms preprocess, 453.7ms inference, 0.7ms postprocess per image at shape (1, 3, 832, 832)

Piezas detectadas: 14

2. RECONSTRUYENDO TABLERO...

TABLERO RECONSTRUIDO:
. . . . . . . .
. . . . . . . p
. p . . N . r .
p . k P . . . K
. . P . . b . P
. P . . . . . .
P . . . R . . .
. . . . . . . .

FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

¿POSICIÓN VÁLIDA?
True

3. ANALIZANDO CON STOCKFISH...

MEJOR JUGADA:
c5b4

NOTACIÓN ALGEBRAICA:
Kb4

EVALUACIÓN:
+940
```

### Análisis de los resultados

La ejecución ha completado correctamente todas las etapas del sistema.

Se han detectado 14 piezas y se ha generado automáticamente el tablero digital correspondiente.

La posición reconstruida se ha representado mediante FEN y ha superado la comprobación de validez de `python-chess`.

Stockfish ha recomendado el movimiento `c5b4`, correspondiente al desplazamiento del rey negro desde `c5` hasta `b4`.

También se ha obtenido una evaluación de `+940` centipeones desde el punto de vista de las blancas.

El turno de las negras se ha establecido manualmente para esta prueba. Por tanto, todavía no se dispone de una identificación automática del turno de juego.

### Conclusiones

Se ha conseguido integrar en un único programa los módulos de reconocimiento visual, reconstrucción digital y análisis de jugadas.

El sistema permite procesar automáticamente una fotografía del tablero y obtener una recomendación de movimiento mediante Stockfish.

Este resultado constituye una primera versión funcional del asistente inteligente de ajedrez sobre una imagen de prueba.

Como siguientes mejoras se plantea representar visualmente la jugada recomendada, incorporar asistencia por voz y realizar pruebas con nuevas fotografías para evaluar la fiabilidad del reconocimiento.

**Estado:** integración automática YOLO + python-chess + Stockfish implementada y comprobada sobre la imagen de ejemplo.


### 7.5. Visualización de la jugada recomendada

Una vez integrada la detección automática mediante YOLO con el motor Stockfish, se ha incorporado una representación gráfica de la jugada recomendada.

El objetivo es facilitar la interpretación del movimiento propuesto mediante una flecha dibujada sobre el tablero digital.

Para ello, se ha utilizado el módulo `chess.svg` de la biblioteca `python-chess` y la biblioteca `cairosvg`, que permite convertir imágenes SVG a formato PNG.

**Instalación de la biblioteca:**

```bash
python -m pip install cairosvg
```

**Código añadido a `asistente_ajedrez.py`:**

```python
import chess.svg
import cairosvg

# Generar tablero con la jugada recomendada
svg = chess.svg.board(
    board=tablero,
    arrows=[
        chess.svg.Arrow(
            mejor_jugada.from_square,
            mejor_jugada.to_square,
            color="#00AA00"
        )
    ],
    orientation=chess.BLACK,
    size=800
)

# Guardar SVG
with open("jugada_recomendada.svg", "w") as archivo:
    archivo.write(svg)

# Convertir a PNG
cairosvg.svg2png(
    bytestring=svg.encode("utf-8"),
    write_to="jugada_recomendada.png"
)

print("\nImagen guardada: jugada_recomendada.png")
```

**Comando ejecutado:**

```bash
python asistente_ajedrez.py
```

**Salida real obtenida (resumen):**

```text
1. DETECTANDO TABLERO Y PIEZAS...

Piezas detectadas: 14

2. RECONSTRUYENDO TABLERO...

FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

¿POSICIÓN VÁLIDA?
True

3. ANALIZANDO CON STOCKFISH...

MEJOR JUGADA:
c5b4

NOTACIÓN ALGEBRAICA:
Kb4

EVALUACIÓN:
+940

Imagen guardada: jugada_recomendada.png
```

**Visualización del resultado:**

```bash
xdg-open jugada_recomendada.png
```

**Imagen generada:**

![Jugada recomendada por Stockfish](../jugada_recomendada.png)

### Análisis de los resultados

Se ha generado correctamente una imagen del tablero digital con las piezas reconocidas por YOLO y una flecha verde que representa el movimiento recomendado por Stockfish.

En esta prueba, el motor ha recomendado la jugada `c5b4`, correspondiente al desplazamiento del rey negro desde `c5` hasta `b4`.

La flecha aparece correctamente situada entre ambas casillas.

El tablero se ha representado desde la perspectiva de las negras, ya que el turno se ha establecido manualmente para este jugador.

### Conclusiones

Se ha conseguido integrar la representación visual de las recomendaciones del motor de ajedrez.

El sistema permite procesar una fotografía del tablero físico, detectar las piezas, reconstruir la posición, analizarla mediante Stockfish y representar gráficamente la jugada recomendada.

Actualmente, la visualización se realiza sobre un tablero digital generado mediante `python-chess`, no directamente sobre la fotografía original.

La siguiente mejora consistirá en incorporar asistencia por voz para comunicar la jugada recomendada al usuario.

**Estado:** visualización de jugadas implementada y comprobada.


### 7.6. Integración de la asistencia por voz

Con el objetivo de mejorar la accesibilidad del asistente de ajedrez, se ha incorporado una funcionalidad de síntesis de voz que permite comunicar al usuario la jugada recomendada por Stockfish.

Para ello, se ha utilizado `espeak-ng`, un sintetizador de voz compatible con Ubuntu.

**Instalación:**

```bash
sudo apt install espeak-ng
```

**Comprobación inicial:**

```bash
espeak-ng -v es "La jugada recomendada es mover el rey negro de ce cinco a be cuatro"
```

Se ha comprobado que el sistema reproduce correctamente el mensaje en español.

### Implementación

Se ha ampliado el archivo `asistente_ajedrez.py` incorporando una función denominada `anunciar_jugada()`.

Esta función identifica la pieza que debe moverse, su color y las casillas de origen y destino.

Posteriormente, construye un mensaje en español y lo reproduce mediante `espeak-ng`.

**Código principal utilizado:**

```python
import subprocess

def anunciar_jugada(tablero, jugada):

    pieza = tablero.piece_at(jugada.from_square)

    nombres_piezas = {
        chess.PAWN: "peón",
        chess.KNIGHT: "caballo",
        chess.BISHOP: "alfil",
        chess.ROOK: "torre",
        chess.QUEEN: "dama",
        chess.KING: "rey"
    }

    nombre_pieza = nombres_piezas[pieza.piece_type]
    color = "blanco" if pieza.color == chess.WHITE else "negro"

    origen = chess.square_name(jugada.from_square)
    destino = chess.square_name(jugada.to_square)

    def pronunciar_casilla(casilla):
        letras = {
            "a": "a", "b": "be", "c": "ce", "d": "de",
            "e": "e", "f": "efe", "g": "ge", "h": "hache"
        }

        return f"{letras[casilla[0]]} {casilla[1]}"

    mensaje = (
        f"La jugada recomendada es mover el "
        f"{nombre_pieza} {color} "
        f"de {pronunciar_casilla(origen)} "
        f"a {pronunciar_casilla(destino)}"
    )

    print("\nASISTENCIA POR VOZ:")
    print(mensaje)

    subprocess.run(
        ["espeak-ng", "-v", "es", "-s", "140", mensaje],
        check=True
    )
```

La función se ejecuta después de obtener la mejor jugada mediante Stockfish.

### Prueba de funcionamiento

**Comando ejecutado:**

```bash
python asistente_ajedrez.py
```

**Salida real obtenida (resumen):**

```text
1. DETECTANDO TABLERO Y PIEZAS...

Piezas detectadas: 14

2. RECONSTRUYENDO TABLERO...

FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

¿POSICIÓN VÁLIDA?
True

3. ANALIZANDO CON STOCKFISH...

MEJOR JUGADA:
c5b4

NOTACIÓN ALGEBRAICA:
Kb4

EVALUACIÓN:
+965

ASISTENCIA POR VOZ:
La jugada recomendada es mover el rey negro de ce5 a be 4

Imagen guardada: jugada_recomendada.png
```

### Análisis de los resultados

La ejecución del programa ha completado correctamente todas las etapas.

Stockfish ha recomendado mover el rey negro desde `c5` hasta `b4`.

Esta recomendación se ha mostrado mediante una flecha sobre el tablero digital y se ha comunicado mediante síntesis de voz.

Se ha confirmado que el mensaje se reproduce correctamente en español.

### Conclusiones

Se ha conseguido incorporar asistencia auditiva al sistema, complementando la representación visual de los movimientos.

Con esta implementación, el asistente dispone de una primera funcionalidad orientada a mejorar la accesibilidad para personas con discapacidad visual.

No obstante, el sistema todavía requiere conocer previamente el turno de juego y utiliza una fotografía de ejemplo.

**Estado:** asistencia por voz implementada y comprobada.

### 7.7. Selección de imágenes mediante argumentos

Para facilitar las pruebas con diferentes fotografías, se ha modificado el programa `asistente_ajedrez.py` para permitir seleccionar la imagen de entrada desde la terminal.

Se ha utilizado la biblioteca `argparse`, que permite gestionar los argumentos proporcionados durante la ejecución.

**Código añadido:**

```python
import argparse

parser = argparse.ArgumentParser(
    description="Asistente inteligente de ajedrez"
)

parser.add_argument(
    "imagen",
    nargs="?",
    default="chess_board_image.jpg",
    help="Ruta de la fotografía del tablero"
)

args = parser.parse_args()

IMAGEN = args.imagen

print(f"\nImagen seleccionada: {IMAGEN}")
```

Se ha establecido `chess_board_image.jpg` como imagen predeterminada, de manera que el argumento sea opcional.

**Ejecución con una imagen especificada:**

```bash
python asistente_ajedrez.py chess_board_image.jpg
```

**Resultado:**

Se ha comprobado que el programa funciona correctamente al proporcionar la ruta de la imagen como argumento.

El asistente mantiene el procesamiento mediante YOLO, la reconstrucción del tablero, el análisis con Stockfish y la asistencia visual y por voz.

**Ejecución sin argumentos:**

```bash
python asistente_ajedrez.py
```

En este caso, el programa está configurado para utilizar automáticamente `chess_board_image.jpg`.

**Conclusión:**

Se ha mejorado la flexibilidad del programa, permitiendo seleccionar distintas fotografías sin modificar el código fuente.

Esta funcionalidad facilitará la realización de pruebas con nuevos tableros y posiciones de ajedrez.

**Estado:** selección de imágenes implementada y comprobada mediante argumento. Ejecución sin argumentos configurada, pendiente de comprobación.

### 7.8. Configuración del turno de juego mediante argumentos

Para mejorar la flexibilidad del asistente, se ha incorporado la posibilidad de seleccionar el jugador al que le corresponde mover directamente desde la terminal.

Anteriormente, el turno estaba establecido manualmente para las negras dentro del código.

Se ha utilizado la biblioteca `argparse` para añadir el argumento opcional `--turno`, que permite seleccionar entre blancas y negras.

**Código añadido en `asistente_ajedrez.py`:**

```python
parser.add_argument(
    "--turno",
    choices=["blancas", "negras"],
    default="negras",
    help="Jugador al que le corresponde mover"
)

args = parser.parse_args()

IMAGEN = args.imagen

TURNO = chess.WHITE if args.turno == "blancas" else chess.BLACK
```

Posteriormente, se ha modificado la creación del tablero para utilizar el turno seleccionado:

```python
tablero = chess.Board(None)
tablero.turn = TURNO
```

También se ha adaptado la representación gráfica para mostrar el tablero desde la perspectiva del jugador correspondiente:

```python
orientation=TURNO,
```

### Pruebas realizadas

**Prueba 1. Ejecución con valores predeterminados**

Comando ejecutado:

```bash
python asistente_ajedrez.py
```

**Salida real obtenida:**

```text
Imagen seleccionada: chess_board_image.jpg
Turno seleccionado: negras

Piezas detectadas: 14

FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

¿POSICIÓN VÁLIDA?
True

MEJOR JUGADA:
c5b4

NOTACIÓN ALGEBRAICA:
Kb4

EVALUACIÓN:
+940

ASISTENCIA POR VOZ:
La jugada recomendada es mover el rey negro de ce5 a be 4

Imagen guardada: jugada_recomendada.png
```

**Prueba 2. Ejecución con argumentos explícitos**

Comando ejecutado:

```bash
python asistente_ajedrez.py chess_board_image.jpg --turno negras
```

**Salida real obtenida:**

```text
Imagen seleccionada: chess_board_image.jpg
Turno seleccionado: negras

Piezas detectadas: 14

FEN:
8/7p/1p2N1r1/p1kP3K/2P2b1P/1P6/P3R3/8 b - - 0 1

¿POSICIÓN VÁLIDA?
True

MEJOR JUGADA:
c5b4

NOTACIÓN ALGEBRAICA:
Kb4

EVALUACIÓN:
+940

ASISTENCIA POR VOZ:
La jugada recomendada es mover el rey negro de ce5 a be 4

Imagen guardada: jugada_recomendada.png
```

### Análisis de los resultados

Ambas ejecuciones han producido resultados equivalentes.

El sistema ha detectado 14 piezas, reconstruido una posición válida y obtenido la misma recomendación de Stockfish.

También se ha generado correctamente la representación gráfica de la jugada y se ha ejecutado la asistencia por voz.

Se confirma que el programa permite configurar tanto la imagen de entrada como el turno mediante argumentos opcionales.

La opción de seleccionar el turno de las blancas todavía no se ha probado con una posición válida para ese jugador.

### Conclusiones

Se ha mejorado la configuración del asistente, permitiendo seleccionar la fotografía y el turno sin modificar el código fuente.

Los valores predeterminados permiten ejecutar directamente la imagen de ejemplo con el turno de las negras.

Esta funcionalidad facilitará las pruebas posteriores con diferentes posiciones de ajedrez.

**Estado:** selección de imagen y turno implementada. Funcionamiento comprobado con los valores predeterminados y con argumentos explícitos.