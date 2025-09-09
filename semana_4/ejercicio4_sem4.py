#4. Cree un programa que le pida tres números al usuario y muestre el mayor.
number_one = int(input("Usuario ingrese el primer número: "))
number_two = int(input("Usuario ingrese el segundo número: "))
number_three = int(input("Usuario ingrese el tercer número: "))

if (number_one > number_two and number_one > number_three):
    print(f"El numero mayor es: {number_one}")
elif (number_two > number_one and number_two > number_three):
    print(f"El número mayor es: {number_two}")
elif (number_one == number_two and number_one > number_three):
    print("Los dos primeros números son iguales y son los mayores")
elif (number_one == number_three and number_one > number_two):
    print("El primer y tercer número son iguales y son los mayores")
elif (number_two == number_three and number_two > number_one):
    print("El segundo y tercer número son iguales y son los mayores")
elif (number_one == number_two == number_three):
    print("Los tres números son iguales")
else:
    print(f"El número mayor es: {number_three}")

#Investigando me di cuneta que hay una función para comparar el número mayor pero para este ejercicio, como son los primeros decidi 
#hacerlo con los condicionales para practicar un poco mas la lógica.
