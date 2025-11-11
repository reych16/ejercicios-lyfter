def show_params_and_result(func):
    def wrapper(*args, **kwargs):
        print("Funtion called with: ", args, kwargs)
        result = func(*args, **kwargs)
        print("Function returned:", result)
        return result
    return wrapper

@show_params_and_result
def add(a, b):
    return a + b

add(3, 4)