#3. Cree un programa que use una lista para eliminar keys de un diccionario.
    #1. Ejemplos:
    #2. `list_of_keys = [’access_level’, ‘age’]`
    #`employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    #→ `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

student = {
    'name' : 'Reychel',
    'last_name' : 'Vargas',
    'age' : 22,
    'career' : 'Software Engineering'
}

list_of_keys = ['last_name', 'age']

for key in list_of_keys:
    if key in student :
        student.pop(key)

print(student)

