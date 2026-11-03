def cache(func):
    notebook = {}

    def wrapper(*args):
        if args in notebook:
            return notebook[args]

        result = func(*args)
        notebook[args] = result
        return result

    return wrapper


@cache
def multiply_numbers(a, b):
    return a * b


print(multiply_numbers(4, 5))
print(multiply_numbers(3, 3))