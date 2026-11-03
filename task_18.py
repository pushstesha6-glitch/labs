import datetime


def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_now = datetime.datetime.now()
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"Время: {time_now} | Функция: {func.__name__} | Аргументы: {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_calls("calls.log")
def add(a, b):
    return a + b


add(2, 3)
add(10, 20)
