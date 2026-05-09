from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[日志] 开始调用函数：{func.__name__}")
        print(f"[日志] args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"[日志] 函数 {func.__name__} 调用结束")
        return result

    return wrapper


@log_call
def create_order(user_id: int, product_id: int):
    print(f"用户 {user_id} 创建商品 {product_id} 的订单")
    return "订单创建成功"


result = create_order(1001, 2002)
print(result)