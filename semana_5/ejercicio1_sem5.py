#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    #1. Ejemplos:
    #2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    #`second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->

first_list = ['Todos', 'dias', 'se', 'que', 'al' ]
second_list = ['los', 'siempre', 'tienen', 'aprovechar', 'maximo']

for index in range (0, len(first_list)):
    word_1 = first_list[index]
    word_2 = second_list[index]
    print(f"{word_1} {word_2}")