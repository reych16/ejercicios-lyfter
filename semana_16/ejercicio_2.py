def sum_list(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total


def reverse_string(my_string):
    invert_string = ''
    for index in range(len(my_string) -1, -1, -1):
        invert_string += my_string[index]
    return invert_string


def count_upper_and_lower(my_string):
    upper_count = 0
    lower_count = 0

    for letter in my_string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    
    return upper_count, lower_count


def sort_words_in_string(my_string):
    word_list = my_string.split('-')
    word_list.sort()
    sorted_string = '-'.join(word_list)
    return sorted_string


def is_prime(number):
    if number < 2:
        return False
    for index in range(2, int(number ** 0.5) + 1):
        if number % index == 0:
            return False
    return True


def get_primes_from_list(numbers_list):
    prime_numbers = []
    for number in numbers_list:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers