#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

import csv
import os

def write_csv_file(file_path, data, headers):
    try: 
        file_exists = os.path.exists(file_path)

        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            if not file_exists:
                writer.writeheader()
            writer.writerows(data)
    except PermissionError as error:
        print(f'No tienes permiso para escribir en {file_path}. Error: {error}')


def main():
    print('=== Registro de Videojuegos a CSV ===')
    try:
        while True: 
            try:
                total_games = int(input('Cuántos videojuegos deseas ingresar? '))
                if total_games <= 0:
                    print('Debe ser un número mayor a 0.')
                else:
                    break
            except ValueError as error:
                print(f'Debes ingresar un número entero valido. Error: {error}')

        games = []
        for index in range(1, total_games + 1):
            print(f'\nVideojuego #{index}')
            name = input('Nombre: ')
            genre = input('Género: ')
            developer = input('Desarrollador: ')
            classification = input('Clasificación ESRB: ')

            games.append({
                'nombre': name,
                'genero': genre,
                'desarrollador': developer,
                'clasificacion': classification,
            })
    
        headers = ['nombre', 'genero', 'desarrollador', 'clasificacion']
        write_csv_file('videojuegos.csv', games, headers)

        print(f"\n Se guardaron {len(games)} videojuegos en 'videojuegos.csv'.")

    except Exception as error:
        print(f'Ocurrió un error inesperado. Error: {error}')

if __name__ == "__main__":
    main()
