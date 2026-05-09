from functools import wraps


def check_positive_amount(func):
    @wraps(func)
    def wrapper(amount: float, *args, **kwargs):
        if amount <= 0:
            raise ValueError("金额必须大于 0")

        return func(amount, *args, **kwargs)

    return wrapper


@check_positive_amount
def pay(amount: float):
    print(f"支付金额：{amount}")


pay(100)
# pay(-1)