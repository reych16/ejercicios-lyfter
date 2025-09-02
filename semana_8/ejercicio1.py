#1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_and_print_file_per_line(path):
    try:
        with open(path, encoding="utf-8") as file:
            for line in file.readlines():
                print(f'Song: {line.strip()}')
    except FileNotFoundError as error:
        print(f'El archivo no existe. Error: {error}')


def sort_songs(input_path):
    try:
        with open(input_path, encoding="utf-8") as file:
            songs = []
            for line in file.readlines():
                title = line.strip()
                if title:
                    songs.append(title)
            songs.sort()
            return songs
    except FileNotFoundError as error:
        print(f'El archivo no existe. Error: {error}')
        return []


def write_sorted_songs(output_path, songs):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            for song in songs:
                file.write(song + "\n")
            print(f'Canciones guardadas en {output_path}')
    except PermissionError as error:
        print(f'No tienes permisos para escribir en {output_path}. Error: {error}')


def main():
    try:
        print('\n--- Canciones en el orden original ---')
        read_and_print_file_per_line('songs.txt')

        sorted_songs = sort_songs('songs.txt')
        if sorted_songs:
            print('\n--- Canciones ordenadas alfabéticamente ---')
            for song in sorted_songs:
                print(f'Song: {song}')
            write_sorted_songs('songs_sorted.txt', sorted_songs)
    except Exception as error: 
        print(f'Ocurrió un error inesperado. Error: {error}')

if __name__ == '__main__':
    main()
