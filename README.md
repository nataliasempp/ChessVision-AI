# ♟️ ChessVision-AI

### Asistente inteligente de ajedrez mediante visión por computador

Proyecto desarrollado para la asignatura **Procesamiento de Imágenes por Computador** del Máster en Robótica y Automatización de la UC3M .

## Descripción

ChessVision-AI es un asistente inteligente capaz de analizar fotografías de un tablero de ajedrez físico y recomendar movimientos utilizando visión por computador e inteligencia artificial.

El objetivo es desarrollar un sistema que reconozca las piezas y su posición, reconstruya digitalmente el tablero y proporcione recomendaciones tanto visualmente como por voz, facilitando su uso a personas con discapacidad visual.

## Funcionamiento

El sistema sigue el siguiente proceso:

1. **YOLO:** detecta las piezas y las esquinas del tablero.
2. **OpenCV:** corrige la perspectiva y determina las casillas.
3. **python-chess:** reconstruye y valida la posición.
4. **Stockfish:** calcula la jugada recomendada.
5. **Asistencia visual y auditiva:** muestra el movimiento mediante una flecha y lo anuncia por voz.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/nataliasempp/ChessVision-AI.git
cd ChessVision-AI
```

Crear el entorno virtual e instalar las dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Instalar Stockfish y el sintetizador de voz en Ubuntu:

```bash
sudo apt install stockfish espeak-ng
```

## Uso

**Ejecución predeterminada:**

```bash
python asistente_ajedrez.py
```

**Seleccionar una imagen y el turno:**

```bash
python asistente_ajedrez.py datos/imagenes/imagen.jpg --turno blancas
```

El turno puede ser `blancas` o `negras`. Por defecto, se utiliza la fotografía de ejemplo y el turno de las negras.

## Estado del proyecto

### ✅ Implementado

- Detección de piezas y tablero mediante YOLO.
- Reconstrucción y validación digital del tablero.
- Análisis de posiciones con Stockfish.
- Visualización de la jugada recomendada.
- Asistencia por voz en español.
- Selección de imagen y turno.

### 🔄 Pendiente

- Pruebas con nuevas fotografías y evaluación de precisión.
- Mejoras en la robustez del reconocimiento.
- Detección automática de la orientación del tablero.
- Seguimiento de partidas y gestión del turno.
- Procesamiento de vídeo en tiempo real.
- Desarrollo de una interfaz de usuario.

**Estado actual:** primera versión funcional, probada con una fotografía de ejemplo.

## Referencias

El reconocimiento de piezas parte del repositorio [Chess Detection Computer Vision](https://github.com/alpkirisci/chess_detection_computer_vision), cuyos modelos preentrenados y código de inferencia se han utilizado como base.

La documentación original se conserva en `docs/README_original.md`.

El código y los modelos reutilizados están sujetos a las condiciones de licencia que les correspondan.