def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, exp_type in zip(args, expected_types):
                if not isinstance(arg, exp_type):
                    raise TypeError(
                        f"Аргумент '{arg}' типа {type(arg).__name__}, ожидался {exp_type.__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b
print("Результат:", add(5, 10))  # Всё ок, выведет 15

try:
    print(add(5, "десять"))
except TypeError as e:
    print("Ошибка поймана:", e)