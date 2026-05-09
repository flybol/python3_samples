

def decorator(fn):
    def wrapper():
        print("执行额外功能")
        fn()
    return wrapper

@decorator
def fnA():
    print("被装饰函数FnA")

fnA()

"""
@decorator 把被装饰的函数名作为参数传递给装饰器函数
然后在装饰器内部函数中调用这个函数对象，实现被装饰函数调用。
"""