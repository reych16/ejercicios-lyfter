#2. Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if (age <= 2):
    print("Eres un bebé")
elif (age <= 6):
    print("Eres un niño")
elif(age <= 12):
    print("Eres un preadolescente")
elif(age <= 17):
    print("Eres un adolescente")
elif(age <= 25):
    print("Eres un adulto joven")
elif(age <= 59):
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")



