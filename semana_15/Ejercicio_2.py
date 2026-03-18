#Exercise 1
#Bubble Sort
def bubble_sort(numbers):
    for pass_number in range(len(numbers) - 1):
        made_changes = False

        for index in range(len(numbers) - 1 - pass_number):

            if numbers[index] > numbers[index +1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                made_changes = True

        if not made_changes:
            break


#Excersise 2
def print_numbers_times_2(numbers_list):
    for number in numbers_list:
        print(number * 2)


#Excersise 3
def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
            
    return False


#Excersise 4
def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)

    for index in range(min(list_len, 10)):
        print(list_to_print[index])


# Exercise 5
def generate_list_trios(list_a, list_b, list_c):

    result_list = []

    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                result_list.append(f"{element_a} {element_b} {element_c}")

    return result_list