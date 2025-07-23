import time
from functools import wraps


def log(filename="consol"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_1 = time.time()
                time_2 = time.time()
                print(f"Начало: {time_1}")
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename == "consol":
                    print(f"Функция {name_func} ок. Результат: {result}")
                else:
                    print(f"{name_func} ok. Результат: {func(*args, **kwargs)}")
            except Exception as e:
                result = None
                print(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
            except ZeroDivisionError:
                result = None
                print(f"{func.__name__} error: ZeroDivisionError. Inputs: {args}, {kwargs}")
            print(f"Конец: {time_2}")
            return result

        return wrapper

    return decorator
