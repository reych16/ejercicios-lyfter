#4. Cree una función que le de la vuelta a un string y lo retorne.
    #“Hola mundo” → “odnum aloH”

def reverse_string(my_string):
    invert_string = ''
    for index in range(len(my_string) -1, -1, -1):
        invert_string += my_string[index]
    return invert_string

print(reverse_string('Mi apodo es Rey'))