
import csv

class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    def to_dict(self):
        return {"titulo": self.titulo, "genero": self.genero, "duracion": self.duracion}

class SistemaAudiovisual:
    def __init__(self):
        self.peliculas = []

    def cargar_peliculas(self, archivo_csv):
        with open(archivo_csv, mode='r') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                self.peliculas.append(Pelicula(fila['titulo'], fila['genero'], fila['duracion']))

    def guardar_peliculas(self, archivo_csv):
        with open(archivo_csv, mode='w', newline='') as archivo:
            fieldnames = ["titulo", "genero", "duracion"]
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            writer.writeheader()
            for pelicula in self.peliculas:
                writer.writerow(pelicula.to_dict())
