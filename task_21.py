import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        ms = (end_time - start_time) * 1000
        print(f"Функция выполнилась за {ms:.3f} мс")

        return result

    return wrapper

@timing
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


print("Результат:", slow_sum(1000000))