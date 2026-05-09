import time
from functools import wraps

def retry(max_attempts:int=3,delay:float=1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"[重试] 第 {attempt} 次调用")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"[重试] 调用失败：{e}")
                    time.sleep(delay)
            
            raise RuntimeError(f"函数 {func.__name__} 重试 {max_attempts} 次后仍然失败") from last_error
        return wrapper
    return decorator




count = 0
@retry(max_attempts=3, delay=1)
def call_api():
    global count
    count += 1

    if count < 3:
        raise ConnectionError("网络异常")

    return "接口调用成功"

print(call_api())