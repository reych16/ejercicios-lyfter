import json

file_path = 'pokemons.json'

def read_pokemon_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                print('El archivo no contiene ninguna lista.')
                return[]
            return data
    except FileNotFoundError as error:
        print(f'No se encontro el archivo {file_path}')


def write_pokemon_list(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f'Archivo actualizado: {file_path}')
    except PermissionError as error:
        print(f'Sin permisos para escribir en {file_path}. Error: {error}')


def get_non_empty(prompt_msg):
        while True:
            value = input(prompt_msg).strip()
            if value:
                return value
            print('Este campo no puede estar vacío.')


def get_int(prompt_msg):
        while True:
            raw = input(prompt_msg).strip()
            try:
                return int(raw)
            except ValueError as error:
                print(f'Debes ingresar un número entero. Error: {error}')


def collect_new_pokemon():
    print('\n=== Nuevo Pokémon ===')
    english_name = get_non_empty('Nombre (inglés): ')

    types_raw = get_non_empty('Tipo(s): ')
    types = [t.strip() for t in types_raw.split(',') if t.strip()]

    print('\n=== Stats base ===')
    hp = get_int('HP: ')
    attack = get_int('Attack: ')
    defense = get_int('Defense: ')
    sp_attack = get_int('Sp. Attack: ')
    sp_defense = get_int('Sp. Defense: ')
    speed = get_int('Speed: ')

    new_pokemon = {
        "name": {"english": english_name},
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    return new_pokemon


def main():
    try:
        pokemon_list = read_pokemon_list(file_path)  # lista existente (o vacía si no hay)

        new_pokemon = collect_new_pokemon()
        pokemon_list.append(new_pokemon)

        write_pokemon_list(file_path, pokemon_list)
        print('✅ Pokémon agregado correctamente.')
    except Exception as error:
        print(f'Ocurrió un error inesperado. Error: {error}')


if __name__ == '__main__':
    main()
