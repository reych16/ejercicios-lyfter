#5. Dada `n` cantidad de notas de un estudiante, calcular:
    #1. Cuantas notas tiene aprobadas (mayor a 70).
    #2. Cuantas notas tiene desaprobadas (menor a 70).
    #3. El promedio de todas.
    #4. El promedio de las aprobadas.
    #5. El promedio de las desaprobadas.

total_grades = int(input("Ingrese la cantidad de notas: "))
grade_counter = 1
approved_count = 0
failed_count = 0
approved_sum = 0
failed_sum = 0
total_average = 0

#Mientras que el contador sea menor o igual al totak de notas
while grade_counter <= total_grades:
    print(f"\nIngrese la nota número {grade_counter}:")
    current_grade = float(input())

    if current_grade < 70:
        failed_count += 1
        failed_sum += current_grade
    else:
        approved_count += 1
        approved_sum += current_grade

    total_average += current_grade / total_grades
    grade_counter += 1

#Calcular promedios
if approved_count > 0:
    approved_average = approved_sum / approved_count
else:
    approved_average = 0

if failed_count > 0:
    failed_average = failed_sum / failed_count
else:
    failed_average = 0

print(f"\nLa cantidad de notas aprobadas es de: {approved_count}")
print(f"El promedio de notas aprobadas es de: {approved_average}")
print(f"La cantidad de notas desaprobadas es de: {failed_count}")
print(f"El promedio de notas desaprobadas es de: {failed_average}")
print(f"El promedio total de notas es de: {total_average}")