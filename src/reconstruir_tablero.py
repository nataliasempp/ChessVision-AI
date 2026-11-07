import chess
import chess.engine

# ==========================================
# 1. PIEZAS DETECTADAS POR YOLO
# ==========================================

# Datos obtenidos durante la primera ejecución
# de chess_inference_example.py.

detecciones = [
    ("c4", "white_pawn"),
    ("e2", "white_rook"),
    ("f4", "black_bishop"),
    ("d5", "white_pawn"),
    ("e6", "white_knight"),
    ("g6", "black_rook"),
    ("h4", "white_pawn"),
    ("h5", "white_king"),
    ("b3", "white_pawn"),
    ("a2", "white_pawn"),
    ("a5", "black_pawn"),
    ("h7", "black_pawn"),
    ("b6", "black_pawn"),
    ("c5", "black_king")
]


# ==========================================
# 2. CONVERSIÓN DE CLASES A SÍMBOLOS
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
# 3. CREACIÓN DEL TABLERO VACÍO
# ==========================================

tablero = chess.Board(None)

# Prueba: establecer el turno de las negras
tablero.turn = chess.BLACK
# ==========================================
# 4. COLOCACIÓN DE LAS PIEZAS
# ==========================================

for posicion, pieza in detecciones:

    casilla = chess.parse_square(posicion)

    simbolo = conversion[pieza]

    tablero.set_piece_at(
        casilla,
        chess.Piece.from_symbol(simbolo)
    )


# ==========================================
# 5. MOSTRAR RESULTADOS
# ==========================================

print("\nTABLERO RECONSTRUIDO:\n")
print(tablero)

print("\nPOSICIÓN FEN:")
print(tablero.fen())

print("\nNÚMERO DE PIEZAS:")
print(len(tablero.piece_map()))

print("\n¿ES UNA POSICIÓN VÁLIDA?")
print(tablero.is_valid())

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


# ==========================================
# 7. ANÁLISIS CON STOCKFISH
# ==========================================

print("\nANÁLISIS CON STOCKFISH:")

# Comprobar que la posición es válida
if tablero.is_valid():

    # Ruta del motor instalado en Ubuntu
    ruta_stockfish = "/usr/games/stockfish"

    # Iniciar Stockfish
    motor = chess.engine.SimpleEngine.popen_uci(
        ruta_stockfish
    )

    try:
        # Analizar la posición durante 2 segundos
        resultado = motor.analyse(
            tablero,
            chess.engine.Limit(time=2.0)
        )

        # Obtener la mejor jugada
        mejor_jugada = resultado["pv"][0]

        print("\nMejor jugada (UCI):")
        print(mejor_jugada.uci())

        print("\nMejor jugada (notación SAN):")
        print(tablero.san(mejor_jugada))

        # Obtener la evaluación
        evaluacion = resultado["score"].white()

        print("\nEvaluación de la posición:")
        print(evaluacion)

    finally:
        # Cerrar correctamente el motor
        motor.quit()

else:
    print("La posición no es válida.")
    print("No se puede realizar el análisis.")