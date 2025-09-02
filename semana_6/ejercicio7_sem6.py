#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

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

print(get_primes_from_list([12, 23, 27, 64, 61, 8, 1]))