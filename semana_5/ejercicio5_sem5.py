#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    #1. Ejemplos:
    #2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

numbers_list = []

for index in range(10):
    num = int(input(f"Ingrese el número {index+1}: "))
    numbers_list.append(num)

largest_number = numbers_list[0]
for num in numbers_list:
    if num > largest_number:
        largest_number = num

print(numbers_list)
print(f"El número más alto fue el: {largest_number}")


