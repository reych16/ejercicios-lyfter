#2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    #1. Ejemplos:
    #2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    #`list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    #→ `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`

first_list = ['first_name', 'last_name', 'age', 'role']
second_list = ['Reychel', 'Vargas', 22, 'Student']

my_dict = {}

for index in range(len(first_list)):
    key = first_list[index]
    value = second_list[index]
    my_dict[key] = value

print(my_dict)