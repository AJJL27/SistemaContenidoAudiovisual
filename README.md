# SistemaContenidoAudiovisual
Este es un sistema básico para gestionar contenido audiovisual como películas, siguiendo los principios de programación orientada a objetos (POO) y buenas prácticas de desarrollo.

Funcionalidades
Cargar Películas desde Archivo: Lee un archivo CSV (peliculas.csv) y crea objetos de tipo Pelicula.
Mostrar Películas: Muestra una lista de las películas cargadas en la terminal.
Guardar Películas en Archivo: Escribe el estado actual de las películas en un nuevo archivo CSV (nuevas_peliculas.csv).
Requisitos
Python 3.8+
Editor recomendado: VS Code
Estructura del Proyecto
bash
Copiar código
SistemaContenidoAudiovisual/
│
├── peliculas.csv          # Archivo de datos inicial
├── models.py              # Clases y lógica del sistema
├── main.py                # Punto de entrada del programa
└── nuevas_peliculas.csv   # Archivo generado tras ejecutar el sistema
Uso
Clona o descarga el proyecto.
Asegúrate de tener instalado Python.
Abre una terminal y navega hasta la carpeta del proyecto.
Ejecuta el programa con:
bash
Copiar código
python main.py
Esto realizará las siguientes acciones:
Cargará las películas desde peliculas.csv.
Mostrará las películas cargadas en la terminal.
Guardará las películas en nuevas_peliculas.csv.
Ejemplo de Datos (peliculas.csv)
El archivo peliculas.csv debe tener el siguiente formato:

Copiar código
titulo,genero,duracion
Matrix,Accion,136
Titanic,Drama,195
Interstellar,Ciencia Ficcion,169
Notas
Este sistema está diseñado para ser ampliado con soporte para otros tipos de contenido (series, documentales, etc.).
Las pruebas unitarias y la implementación del patrón MVC se pueden agregar en futuras etapas.
