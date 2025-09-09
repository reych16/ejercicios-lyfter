#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    #1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_upper_and_lower(my_string):
    upper_count = 0
    lower_count = 0

    for letter in my_string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1

    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")

count_upper_and_lower('I love to play Handball')


