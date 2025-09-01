#Manejo de archivos no recomendado
#def open_and_print_file(path):
#	file = open(path)
#	print(file.read())

#open_and_print_file('hello.txt')

#Manera correcta de leer los archivos
def open_and_print_file(path):
	with open(path) as file:
		print(file.read())

	print("La variable 'file' ya no existe")
	print('El archivo ya no esta abierto')

open_and_print_file('hello.txt')


#Leer un archivo de varias lineas, linea por linea
def open_and_print_file_per_line(path):
	with open(path) as file:
		for line in file.readlines():
			print(f'Linea: {line}')

open_and_print_file_per_line('superheroes.txt')


#Escritura de archivos usando modo a
from datetime import datetime


def generate_time_log():
    current_time = datetime.now()
    return 'Esto fue escrito a las ' + current_time.strftime('%I:%M %p')

def write_time_log_to_file(file_path):
    log = generate_time_log()
    with open(file_path, 'a') as file:
        file.write(log)

write_time_log_to_file('time_entries.log')


#Escritura de archivos usando modo w
from datetime import datetime


def generate_time_log():
    current_time = datetime.now()
    return 'Esto fue escrito a las ' + current_time.strftime('%I:%M %p')

def write_time_log_to_file(file_path):
    log = generate_time_log()
    with open(file_path, 'w') as file:
        file.write(log)

write_time_log_to_file('time_entries.log')


#Escritura de texto en español con encoding
def write_text_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

text_to_write = """
Tradicionalmente, el número de especies de pingüinos a nivel mundial es de 17.
En 2006, se cambió este número a 18, cuando se empezó a reconocer al
pingüino saltarrocas como dos especies distintas:
el pingüino saltarrocas austral y el pingüino saltarrocas norteño.
"""
write_text_to_file("penguins.txt", text_to_write)