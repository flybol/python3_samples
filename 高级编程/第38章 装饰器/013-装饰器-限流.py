import time
from functools import wraps


def rate_limit(interval: int):
    last_call_time = 0

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call_time

            now = time.time()

            if now - last_call_time < interval:
                raise RuntimeError(f"调用太频繁，请 {interval} 秒后再试")

            last_call_time = now
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(interval=3)
def send_sms(phone: str):
    print(f"发送短信验证码到：{phone}")


send_sms("13800138000")
# 立刻再次调用会报错
send_sms("13800138000")