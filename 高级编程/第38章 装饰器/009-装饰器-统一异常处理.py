from functools import wraps


def handle_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"[业务异常] {e}")
            return None
        except Exception as e:
            print(f"[系统异常] {e}")
            return None

    return wrapper


@handle_exception
def divide(a: int, b: int):
    if b == 0:
        raise ValueError("除数不能为 0")

    return a / b


print(divide(10, 2))
print(divide(10, 0))