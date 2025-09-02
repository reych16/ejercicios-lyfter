#1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
#Por ejemplo:
    #1. string + string → ?
    #2. string + int → ?
    #3. int + string → ?
    #4. list + list → ?
    #5. string + list → ?
    #6. float + int → ?
    #7. bool + bool → ?

#string + string
print("Hola" + " Mundo")

my_name = "Reychel" 
last_name = " Vargas"
print(f"{my_name}{last_name}")

my_second_name = " De Nazareth"
print(my_name + my_second_name + last_name)

my_age = 22
#String + int
#print(my_name + my_age) No funciona porque Python no puede mezclar texto con número
#print(my_name + str(my_age)) Si funciona pero es mejor la otra opción
print(f"{my_name}{my_age}")

#int + String
#print(22 + my_name) No funciona porque el número intenta sumar pero se encuentra con un str
print(int("22") + 5) #Aqui lo que hace es que el 22 que es un texto lo convierte a número y ya lo suma 
print("22" + str(5)) #22 es un string, y str(5) convierte el número 5 en texto y luego python hace una concatenación de texto, es decir, NO se está sumando
print(f"{my_age}5")
#print(f"{my_age} + 5") Imprime 22 + 5

#list + list 
my_first_list = [2, 5, 8]
other_list = [7, 6, 1]
print(my_first_list + other_list)
print(f"{my_first_list}{other_list}")

#String + list
#print("Hola" + [1, 3, 3])Python no sabe que hacer porque son tipos incompatibles directamente
print(f"{my_name}{my_first_list}") 
print(["Hola"] + [1, 2, 3])

#float + int
number_float = 3.5
number_int = 4
print(number_float+number_int)
print(4.6 + 2)
print(f"{number_float}{number_int}")#Se convierte en concatenación de texto = 3.54

#bool + bool
print(True + False)
print(True + True)
print(False + False)
print(5 + True)
print(2 + False)



