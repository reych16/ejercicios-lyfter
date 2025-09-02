#3. Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    #2. [4, 6, 2, 29] → 41

def sum_list(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total
        

print(sum_list([15, 8, 16, 4]))
