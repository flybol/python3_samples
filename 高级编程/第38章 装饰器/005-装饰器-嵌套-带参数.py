
from functools import wraps
def name_decoratorA(a:int,b:int):
    def decorator(func):
        print("执行函数：decoratorA")
        @wraps(func)
        def wrapper(msg:str):
            print("执行装饰器：name_decoratorA")
            func(msg)
        return wrapper
    return decorator

def name_decoratorB(url:str):
    def decorator(fn):
        print("执行函数：decoratorB")
        @wraps(fn)
        def wrapper(msg):
            print("执行装饰器：name_decoratorB")
            fn(msg) # 注意：fn 等于 decoratorA 中的 wrapper
        return wrapper
    return decorator


@name_decoratorB("/api/users")
@name_decoratorA(1,2)
def hello(msg):
    print(f"执行被装饰函数：{msg}")

hello("你好！")

#嵌套装饰器原理分析
# 首先执行最内层的可调用对象
# 返回最内层的可调用对象，作为上一层的参数，上一层可调用对象返回
# 上一层可调用对象返回执行，函数内部语句
# 上一层可调用对象接收的参数是最内层的可调用对象
# 执行最内层的可调用对象

"""
from functools import wraps


def 装饰器业务名(装饰器参数):
    def decorator(func):
    # 装饰后原函数的信息会丢失。
    # print(say_hello.__name__) 输出wrapper
    # 加了：被装饰函数名
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 前置逻辑
            result = func(*args, **kwargs)
            # 后置逻辑
            return result

        return wrapper

    return decorator 
"""