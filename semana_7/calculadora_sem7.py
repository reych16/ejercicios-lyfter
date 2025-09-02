#. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#   1. Suma
#   2. Resta
#   3. Multiplicación
#   4. División
#   5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def show_menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Borrar resultado")
    print("6. Salir")


def get_option():
    while True:
        option_str = input('Elige una opción (1-6): ')
        try: 
            option = int(option_str)
            if 1 <= option <= 6:
                return option
            print('Opción fuera de rango. Debe ser entre 1 y 6.')
        except ValueError as ex:
            print(f'Entrada inválida. Escribe un número entero. {ex}')


def get_number():
    while True:
        value_str = input('Ingresa el número: ')
        try:
            return float(value_str)
        except ValueError as ex:
            print(f'Entrada inválida. Ingrese un número válido. {ex}')


def sum_numbers(current_number, number):
    return current_number + number


def subtract_numbers(current_number, number):
    return current_number - number


def multiply_numbers(current_number, number):
    return current_number * number


def divide_numbers(current_number, number):
    try:
        if number == 0:
            raise ZeroDivisionError('No se puede dividir entre 0.')
        return current_number / number
    except ZeroDivisionError as ex:
        print(f'Error en divide_numbers: {ex}')
        return None


def clear_result():
    return 0.0


def main():
    try:
        current_number = 0.0

        while True:
            print(f'\nNúmero actual: {current_number}')
            show_menu()
            option = get_option()

            if option == 6: 
                print('Saliendo de la calculadora. ¡Hasta luego!')
                break

            if option == 5:
                current_number = clear_result()
                print('Resultado reiniciado a 0')
                continue

            number = get_number()

            if option == 1:
                current_number = sum_numbers(current_number, number)
            elif option == 2:
                current_number = subtract_numbers(current_number, number)
            elif option == 3:
                current_number = multiply_numbers(current_number, number)
            elif option == 4: 
                result = divide_numbers(current_number, number)
                if result is not None:
                    current_number = result

                print(f'Nuevo número actual: {current_number}')

    except Exception as ex:
        print(f'Ocurrió un error inesperado: {ex}')

main()