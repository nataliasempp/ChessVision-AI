# ChessVision-AI ♟️

### Asistente inteligente de ajedrez mediante visión por computador

Proyecto desarrollado para la asignatura **Procesamiento de Imágenes por Computador** del Máster en Robótica y Automatización de la Universidad Carlos III de Madrid (UC3M).

## 1. Descripción del proyecto

**ChessVision-AI** es un asistente inteligente de ajedrez que utiliza técnicas de visión por computador para reconocer las piezas de un tablero físico y recomendar movimientos mediante el motor Stockfish.

El objetivo es desarrollar un sistema que permita analizar una posición de ajedrez a partir de una fotografía y comunicar la jugada recomendada tanto visualmente como mediante síntesis de voz.

Esta última funcionalidad busca facilitar el acceso a la información a personas con discapacidad visual.

El sistema se plantea como una herramienta de entrenamiento y asistencia para situaciones en las que está permitido utilizar análisis externo.

### Funcionamiento general

```text
Fotografía del tablero físico
              |
              v
     Detección mediante YOLO
              |
              v
    Identificación de las piezas
       y de sus coordenadas
              |
              v
   Reconstrucción digital del tablero
              |
              v
    Validación con python-chess
              |
              v
       Análisis con Stockfish
              |
              v
     Recomendación de jugada
              |
       +------+------+
       |             |
       v             v
  Flecha visual   Síntesis de voz
```

## 2. Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python | Desarrollo del sistema |
| YOLO (Ultralytics) | Detección de esquinas y piezas |
| OpenCV | Procesamiento de imágenes y homografía |
| NumPy | Operaciones numéricas |
| python-chess | Representación y validación del tablero |
| Stockfish | Análisis de posiciones y recomendación de movimientos |
| CairoSVG | Generación de imágenes del tablero |
| eSpeak NG | Síntesis de voz en español |
| Git y GitHub | Control de versiones y desarrollo colaborativo |

## 3. Estado actual del proyecto

### Funcionalidades implementadas

- [x] Detección de las piezas mediante YOLO.
- [x] Detección de las esquinas del tablero.
- [x] Transformación de perspectiva mediante homografía.
- [x] Asignación de coordenadas a las piezas.
- [x] Reconstrucción digital del tablero.
- [x] Generación de la posición FEN.
- [x] Validación de la posición mediante `python-chess`.
- [x] Integración con Stockfish.
- [x] Obtención de la jugada recomendada.
- [x] Visualización de la jugada mediante una flecha.
- [x] Reproducción de la recomendación mediante voz.
- [x] Selección de la fotografía de entrada.
- [x] Selección manual del turno de juego.

### Funcionalidades pendientes

- [ ] Realizar pruebas con diferentes fotografías.
- [ ] Evaluar la precisión del reconocimiento de piezas y casillas.
- [ ] Mejorar la detección ante diferentes perspectivas e iluminaciones.
- [ ] Automatizar la orientación de las coordenadas para distintos tableros.
- [ ] Gestionar el turno y el estado de la partida.
- [ ] Mostrar la recomendación directamente sobre la fotografía original.
- [ ] Incorporar procesamiento de vídeo.
- [ ] Desarrollar una interfaz de usuario.
- [ ] Evaluar posibles mejoras o ajustes de los modelos YOLO.

**Estado actual:** primera versión funcional comprobada con una fotografía de ejemplo. El sistema todavía no se ha validado con un conjunto de imágenes diferentes.

## 4. Estructura del repositorio

```text
ChessVision-AI/
│
├── datos/
│   ├── imagenes/            # Fotografías de entrada
│   └── anotaciones/         # Anotaciones de los conjuntos de datos
│
├── docs/                    # Documentación del proyecto
│
├── entrenamiento/           # Scripts y notebooks de entrenamiento
│
├── models/                  # Modelos YOLO preentrenados
│
├── resultados/
│   ├── detecciones/         # Detecciones sobre fotografías
│   ├── homografia/          # Transformaciones de perspectiva
│   └── jugadas/             # Tableros con movimientos recomendados
│
├── src/
│   ├── chess_inference_example.py
│   ├── reconstruir_tablero.py
│   └── visualizar_homografia.py
│
├── asistente_ajedrez.py     # Programa principal
├── requirements.txt         # Dependencias de Python
├── README.md
└── .gitignore
```

## 5. Instalación

Las instrucciones siguientes están orientadas a Ubuntu.

### 5.1. Clonar el repositorio

```bash
git clone https://github.com/nataliasempp/ChessVision-AI.git
cd ChessVision-AI
```

### 5.2. Crear y activar un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
``