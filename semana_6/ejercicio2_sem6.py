#2. Experimente con el concepto de scope:
    #1. Intente accesar a una variable definida dentro de una función desde afuera.
    #2. Intente accesar a una variable global desde una función y cambiar su valor.

def countries():
    country_of_birth = 'Costa Rica'
    print(f'País de Nacimiento: {country_of_birth}')

countries()


country_of_residence = 'Costa Rica'

def print_country_of_residence():
    global country_of_residence
    country_of_residence = 'Colombia'
    print(f'País de residencia: {country_of_residence}')

print_country_of_residence()

print(f'País de residencia: {country_of_residence}')