def only_numbers(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers.")
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers.")
        return func(*args, **kwargs)
    return wrapper

@only_numbers
def multiply(a, b):
    return a * b

print(multiply(3, 6))