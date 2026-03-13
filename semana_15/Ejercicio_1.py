def bubble_sort(numbers):
    for pass_number in range(len(numbers) - 1):
    
        made_changes = False

        for index in range(len(numbers) - 1 - pass_number):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

                made_changes = True
        
        if not made_changes:
            break

def bubble_sort_right_to_left(numbers):
    for pass_number in range(len(numbers) - 1):

        made_changes = False

        for index in range(len(numbers) - 1, pass_number, -1):
            if numbers[index - 1] > numbers[index]:
                numbers[index - 1], numbers[index] = numbers[index], numbers[index - 1]
                made_changes = True
        
        if not made_changes:
            break

test_list_1 = [1, 2, 3, 4, 5, 10, 6, 9, 8]
test_list_2 = [2, 1, 3, 4, 5, 10, 6, 9, 8]

print(f'Original list: {test_list_1}')

bubble_sort(test_list_1)
print(f'Sorted (left to right): {test_list_1}')

bubble_sort_right_to_left(test_list_2)
print(f'Sorted (right to left): {test_list_2}')