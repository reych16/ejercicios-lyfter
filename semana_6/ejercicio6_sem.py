#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def sort_words_in_string(my_string):
    word_list = my_string.split('-')
    word_list.sort()
    sorted_string = '-'.join(word_list)
    return sorted_string
print(sort_words_in_string('python-variable-funcion-computadora-monitor'))