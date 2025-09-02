#3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    #1. Ejemplos:
    #2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`

my_list = [16, 3, 5, 7, 2]

temp_number = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp_number

print(my_list)
