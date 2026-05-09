

def decorator(fn):
    # 这个被包装的函数，本质上就是一个可调用对象
    def wrapper(a:int,b:int):
        print("执行额外功能")
        fn(a,b)
    return wrapper

@decorator
def add(a:int,b:int):
    print(f"计算机结果：{a}+{b}={a+b}")

# add(1,2)
wrapper_addr = decorator(add)
wrapper_addr(1,2)
# 推导
# def wrapper(add)(a:int,b:int):pass

# 本质上通过@decorator 返回可调用对象，然后通过调用这个可调用对象，执行add
# print("wrapper_addr= ",id(wrapper_addr))


