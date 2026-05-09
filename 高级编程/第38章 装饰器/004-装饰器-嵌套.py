

def decoratorA(fn):
    print("执行函数：decoratorA")
    def wrapper():
        print("执行装饰器：decoratorA")
        fn()
    return wrapper

def decoratorB(fn):
    print("执行函数：decoratorB")
    def wrapper():
        print("执行装饰器：decoratorB")
        fn() # 注意：fn 等于 decoratorA 中的 wrapper
    return wrapper


@decoratorB
@decoratorA
def hello():
    print("执行被装饰函数：hello")

hello()

#原理分析
# def decoratorB(decoratorA(fn))()
# decoratorA(fn) 返回 wrapperA 可调用对象
# decoratorB(wrapperA) 返回 wrapperB 可调用对象
# wrapperB()-->执行decoratorB中的wrapper