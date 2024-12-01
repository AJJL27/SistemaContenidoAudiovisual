
from models import SistemaAudiovisual

def main():
    sistema = SistemaAudiovisual()
    # Cargar las películas desde el archivo
    sistema.cargar_peliculas('peliculas.csv')
    print("Películas cargadas:")
    for pelicula in sistema.peliculas:
        print(f"- {pelicula.titulo} ({pelicula.genero}, {pelicula.duracion} min)")
    
    # Guardar en un nuevo archivo
    sistema.guardar_peliculas('nuevas_peliculas.csv')
    print("Películas guardadas en 'nuevas_peliculas.csv'.")

if __name__ == "__main__":
    main()
