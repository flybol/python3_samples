

def decorator(a:int,b:int):
    def wrapped(fn):
        def wrapper(msg:str):
            print(f"接收装饰器参数：a={a}，b={b}")
            fn(msg)
        return wrapper
    return wrapped

@decorator(a=1,b=2)
def hello(msg:str):
    print("打招呼：",msg)

hello("你好！")
#底层逻辑
# decorator(a=1,b=2) 返回 wrapped
# 把当前函数名传给 wrapped(fn) 返回 代理的可调用对象
# wrapper(msg:str) 与 hello(msg:str) 函数签名一样