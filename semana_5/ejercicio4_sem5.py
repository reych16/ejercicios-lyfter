#4. Cree un programa que elimine todos los números impares de una lista.
    #1. Ejemplos:
    #2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list = [12, 3, 5, 6, 8, 10, 11]
even_numbers = []

for number in my_list:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
