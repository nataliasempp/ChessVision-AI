# DESARROLLO DEL PROYECTO

## 1. Introducción

El objetivo del proyecto es desarrollar un asistente inteligente de ajedrez capaz de reconocer un tablero físico mediante técnicas de visión por computador, identificar las piezas y reconstruir digitalmente la posición de una partida.

A partir de esta información, se integrará el motor de ajedrez Stockfish para analizar la posición y recomendar una jugada.

El sistema estará dirigido tanto a personas con visión como a personas con discapacidad visual, por lo que se plantea incorporar una interfaz gráfica y un sistema de comunicación por voz.

## 2. Preparación del entorno de desarrollo

### 2.1. Sistema operativo y herramientas

El desarrollo se realizará en Ubuntu, utilizando Python como lenguaje principal de programación.

Las principales herramientas previstas son:

- **Python:** desarrollo e integración de los distintos módulos.
- **OpenCV:** procesamiento de imágenes y detección del tablero.
- **YOLO:** reconocimiento y localización de las piezas de ajedrez.
- **PyTorch:** ejecución y posible entrenamiento de modelos de aprendizaje profundo.
- **python-chess:** gestión del estado de la partida y validación de movimientos.
- **Stockfish:** análisis de posiciones y recomendación de jugadas.
- **Síntesis de voz:** comunicación de resultados para mejorar la accesibilidad.

### 2.2. Repositorio de referencia

Como punto de partida se ha seleccionado el repositorio público *Chess Detection Computer Vision*.

Repositorio: https://github.com/alpkirisci/chess_detection_computer_vision

Este proyecto utiliza modelos YOLOv8 para detectar las piezas de ajedrez y localizar las esquinas del tablero.

Se estudiará su funcionamiento como base para desarrollar un sistema propio que incorpore la reconstrucción de posiciones, el análisis inteligente de jugadas y la comunicación visual y auditiva.

### 2.3. Estrategia de desarrollo

Se plantea un desarrollo progresivo dividido en las siguientes fases:

1. Estudio y ejecución del sistema de reconocimiento existente.
2. Evaluación del reconocimiento sobre imágenes del repositorio.
3. Reconstrucción digital de las posiciones detectadas.
4. Integración del motor Stockfish.
5. Implementación de la interfaz gráfica y la asistencia por voz.
6. Adaptación del sistema para procesar vídeos capturados con un teléfono móvil.
7. Evaluación del modelo con imágenes propias y posible ajuste fino mediante *fine-tuning*.

Inicialmente se utilizarán imágenes del repositorio, evitando depender de la disponibilidad de un tablero físico.

Posteriormente, se estudiará el funcionamiento del sistema en condiciones de captura reales.

### 2.4. Estado actual

Se ha definido la arquitectura general del proyecto y seleccionado un repositorio de referencia.

El siguiente paso consiste en preparar el entorno de desarrollo en Ubuntu, descargar el código y comprobar la disponibilidad de los modelos preentrenados necesarios para ejecutar las primeras pruebas.

Todavía no se han realizado experimentos de reconocimiento ni se dispone de resultados cuantitativos.

## 3. Implementación inicial del sistema de reconocimiento de piezas

### 3.1. Preparación del entorno

El desarrollo del proyecto se está realizando en Ubuntu, utilizando Python y un entorno virtual para gestionar las dependencias.

Se ha descargado el repositorio público *Chess Detection Computer Vision*, que contiene una implementación de reconocimiento de tableros de ajedrez basada en modelos YOLOv8.

Se han instalado las librerías necesarias para ejecutar el sistema, entre ellas PyTorch, Ultralytics, OpenCV, NumPy y Matplotlib.

### 3.2. Modelos utilizados

El repositorio incluye dos modelos preentrenados que realizan tareas diferentes:

- **Modelo de detección de esquinas (`corner_best.pt`):** permite localizar las cuatro esquinas del tablero y obtener la información geométrica necesaria para identificar las casillas.
- **Modelo de detección de piezas (`piece_best.pt`):** permite identificar y localizar las diferentes piezas de ajedrez mediante técnicas de detección de objetos.

La combinación de ambos modelos permite relacionar las piezas detectadas con las coordenadas de las casillas del tablero.

### 3.3. Primera ejecución

Se ha ejecutado el archivo `chess_inference_example.py` utilizando la imagen de ejemplo `chess_board_image.jpg`, incluida en el repositorio.

El sistema ha conseguido cargar ambos modelos, identificar cuatro esquinas del tablero y detectar un total de 14 piezas.

Los resultados de detección han sido:

| Pieza | Cantidad detectada |
|---|---:|
| Peones blancos | 5 |
| Torre blanca | 1 |
| Caballo blanco | 1 |
| Rey blanco | 1 |
| Peones negros | 3 |
| Torre negra | 1 |
| Alfil negro | 1 |
| Rey negro | 1 |
| **Total** | **14** |

Además de identificar las piezas, el programa ha generado una estructura de datos que incluye la clase de cada pieza, su casilla asignada y la confianza asociada a la detección.

Las confianzas obtenidas para las 14 detecciones se encuentran aproximadamente entre el 94 % y el 96 %.

### 3.4. Resultados obtenidos

La primera ejecución ha finalizado correctamente y ha generado el archivo `annotated_chess_board.jpg`, que contiene la visualización de las detecciones realizadas.

También se ha obtenido una representación estructurada del tablero mediante coordenadas algebraicas, como A1, B4 o F7.

Esto constituye un primer paso hacia la reconstrucción digital de una posición de ajedrez, necesaria para la posterior integración con el motor Stockfish.

### 3.5. Limitaciones y próximos pasos

Aunque la ejecución del sistema ha finalizado correctamente, todavía es necesario comprobar visualmente si todas las piezas se han identificado y localizado de manera correcta.

Las puntuaciones de confianza proporcionadas por YOLO no permiten determinar por sí solas la precisión real del sistema.

Por tanto, el siguiente paso consistirá en analizar la imagen anotada y comprobar las detecciones obtenidas.

Posteriormente, se estudiará la conversión de los resultados a una representación digital de la posición mediante notación FEN, así como su integración con el motor de ajedrez Stockfish.