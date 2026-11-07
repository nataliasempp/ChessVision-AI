import chess
import chess.engine
import chess.svg
import cairosvg
import subprocess
import argparse

from src.chess_inference_example import detect_chess_pieces

# ==========================================
# 0. ASISTENCIA POR VOZ
# ==========================================

def anunciar_jugada(tablero, jugada):

    # Obtener la pieza que se va a mover
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

    # Adaptar las coordenadas para pronunciarlas en español
    def pronunciar_casilla(casilla):

        letras = {
            "a": "a",
            "b": "be",
            "c": "ce",
            "d": "de",
            "e": "e",
            "f": "efe",
            "g": "ge",
            "h": "hache"
        }

        letra = letras[casilla[0]]
        numero = casilla[1]

        return f"{letra} {numero}"

    origen_voz = pronunciar_casilla(origen)
    destino_voz = pronunciar_casilla(destino)

    mensaje = (
        f"La jugada recomendada es mover el "
        f"{nombre_pieza} {color} "
        f"de {origen_voz} a {destino_voz}"
    )

    print("\nASISTENCIA POR VOZ:")
    print(mensaje)

    subprocess.run(
        ["espeak-ng", "-v", "es", "-s", "140", mensaje],
        check=True
    )

# ==========================================
# 1. CONFIGURACIÓN
# ==========================================

# ==========================================
# SELECCIÓN DE LA IMAGEN
# ==========================================

# ==========================================
# CONFIGURACIÓN DE ARGUMENTOS
# ==========================================

parser = argparse.ArgumentParser(
    description="Asistente inteligente de ajedrez"
)

# Imagen de entrada (opcional)
parser.add_argument(
    "imagen",
    nargs="?",
    default="datos/imagenes/chess_board_image.jpg",
    help="Ruta de la fotografía del tablero"
)

# Turno del jugador (opcional)
parser.add_argument(
    "--turno",
    choices=["blancas", "negras"],
    default="negras",
    help="Jugador al que le corresponde mover"
)

args = parser.parse_args()

IMAGEN = args.imagen

TURNO = chess.WHITE if args.turno == "blancas" else chess.BLACK

print(f"\nImagen seleccionada: {IMAGEN}")
print(f"Turno seleccionado: {args.turno}")

MODELO_PIEZAS = "models/piece_best.pt"
MODELO_ESQUINAS = "models/corner_best.pt"

STOCKFISH = "/usr/games/stockfish"


# ==========================================
# 2. CONVERSIÓN DE CLASES YOLO
# ==========================================

conversion = {
    "white_pawn": "P",
    "white_rook": "R",
    "white_knight": "N",
    "white_bishop": "B",
    "white_queen": "Q",
    "white_king": "K",

    "black_pawn": "p",
    "black_rook": "r",
    "black_knight": "n",
    "black_bishop": "b",
    "black_queen": "q",
    "black_king": "k"
}


# ==========================================
# 3. DETECCIÓN AUTOMÁTICA CON YOLO
# ==========================================

print("\n1. DETECTANDO TABLERO Y PIEZAS...")

resultado = detect_chess_pieces(
    model_path=MODELO_PIEZAS,
    image_path=IMAGEN,
    corner_model_path=MODELO_ESQUINAS
)

detecciones = resultado["board_state"]

print(f"\nPiezas detectadas: {len(detecciones)}")


# ==========================================
# 4. RECONSTRUCCIÓN DIGITAL
# ==========================================

print("\n2. RECONSTRUYENDO TABLERO...")

tablero = chess.Board(None)

# Establecer el turno indicado por el usuario
tablero.turn = TURNO

for deteccion in detecciones:

    posicion = deteccion["position"]
    pieza = deteccion["piece"]

    if pieza not in conversion:
        print(f"Clase desconocida: {pieza}")
        continue

    casilla = chess.parse_square(posicion)

    tablero.set_piece_at(
        casilla,
        chess.Piece.from_symbol(conversion[pieza])
    )

print("\nTABLERO RECONSTRUIDO:")
print(tablero)

print("\nFEN:")
print(tablero.fen())

print("\n¿POSICIÓN VÁLIDA?")
print(tablero.is_valid())


# ==========================================
# 5. ANÁLISIS CON STOCKFISH
# ==========================================

if tablero.is_valid():

    print("\n3. ANALIZANDO CON STOCKFISH...")

    motor = chess.engine.SimpleEngine.popen_uci(
        STOCKFISH
    )

    try:
        resultado_motor = motor.analyse(
            tablero,
            chess.engine.Limit(time=2.0)
        )

        mejor_jugada = resultado_motor["pv"][0]

        print("\nMEJOR JUGADA:")
        print(mejor_jugada.uci())

        print("\nNOTACIÓN ALGEBRAICA:")
        print(tablero.san(mejor_jugada))

        print("\nEVALUACIÓN:")
        print(resultado_motor["score"].white())

        # ==========================================
        # ANUNCIAR LA JUGADA RECOMENDADA
        # ==========================================

        anunciar_jugada(tablero, mejor_jugada)

    finally:
        motor.quit()

else:

    print("\nERROR: la posición reconstruida no es válida.")
    print("No se puede analizar con Stockfish.")


# ==========================================
# 6. VISUALIZACIÓN DE LA JUGADA RECOMENDADA
# ==========================================

# Generar tablero con una flecha
svg = chess.svg.board(
    board=tablero,
    arrows=[
        chess.svg.Arrow(
            mejor_jugada.from_square,
            mejor_jugada.to_square,
            color="#00AA00"
        )
    ],
    orientation=TURNO,
    size=800
)

# Guardar SVG
with open("resultados/jugadas/jugada_recomendada.svg", "w") as archivo:
    archivo.write(svg)

# Convertir a PNG
cairosvg.svg2png(
    bytestring=svg.encode("utf-8"),
    write_to="resultados/jugadas/jugada_recomendada.png"
)

print("\nImagen guardada: jugada_recomendada.png")