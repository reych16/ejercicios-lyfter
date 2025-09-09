#Programa que guarda videojuegos en un archivo TSV (tab-separated values)

import csv
import os

def write_tsv_file(file_path, data, headers):
    try:
        file_exists = os.path.exists(file_path)

        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers, delimiter='\t')
            if not file_exists:
                writer.writeheader()
            writer.writerows(data)

    except PermissionError as error:
        print(f'No tienes permiso para escribir en {file_path}. Error: {error}')


def main():
    print('=== Registro de Videojuegos a TSV ===')
    try:
        while True:
            try:
                total_games = int(input('Cuántos videojuegos deseas ingresar? '))
                if total_games <= 0:
                    print('Debe ser un número mayor a 0.')
                else:
                    break
            except ValueError as error:
                print(f'Debes ingresar  un número entero válido. Error: {error}')

        games = []
        for index in range(1, total_games + 1):
            print(f'\nVideojuego #{index}')
            name = input('Nombre: ')
            genre = input('Género: ')
            developer = input('Desarrollador: ')
            classification = input('Clasificación: ')

            games.append({
                'nombre': name,
                'genero': genre,
                'desarrollador': developer,
                'clasificacion': classification,
            })

        headers = ['nombre', 'genero', 'desarrollador', 'clasificacion']
        write_tsv_file('videojuegos.tsv', games, headers)

        print(f"\nSe guardaron {len(games)} videojuegos en 'videojuegos.tsv'.")
    
    except Exception as error:
        print(f'Ocurrió un error inesperado. Error: {error}')

if __name__ == "__main__":
    main()