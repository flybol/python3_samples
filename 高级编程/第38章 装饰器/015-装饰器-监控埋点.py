from functools import wraps


def monitor(event_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[监控] 上报事件：{event_name}，函数：{func.__name__}")

            try:
                result = func(*args, **kwargs)
                print(f"[监控] 事件 {event_name} 执行成功")
                return result
            except Exception as e:
                print(f"[监控] 事件 {event_name} 执行失败：{e}")
                raise

        return wrapper

    return decorator


@monitor("create_order")
def create_order():
    print("创建订单逻辑")


create_order()