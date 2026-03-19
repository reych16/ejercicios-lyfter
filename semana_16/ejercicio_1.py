def bubble_sort(numbers):
    #validar que sea una lista
    if not isinstance(numbers, list):
        raise TypeError("Parameter must be a list")
    
    for pass_number in range(len(numbers) - 1):
        made_changes = False

        for index in range(len(numbers) - 1 - pass_number):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                made_changes = True

        if not made_changes:
            break

    return numbers