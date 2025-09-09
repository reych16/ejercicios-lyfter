#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    #1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute. (Usar una función randint)
import random

secret_number = random.randint(1, 10)
number = int(input("Usuario ingrese un número entre el 1 y 10: "))

while (number != secret_number):
    number = int(input("Ingrese nuevamente otro número: "))


print("Has adivinado el número!")