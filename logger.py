import time


def timer(func):
    def wrapper(*args,  **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Функция {func.__name__} выполнена за {elapsed_time:.2f} секунд.")
        return result
    return wrapper
