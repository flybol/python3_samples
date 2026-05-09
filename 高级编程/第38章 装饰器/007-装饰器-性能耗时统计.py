import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 不受系统时间调整影响
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        cost = end_time - start_time
        print(f"[性能] 函数 {func.__name__} 耗时：{cost:.4f} 秒")
        return result
    return wrapper

@timer
def export_report():
    print("正在导出报表...")
    time.sleep(2)
    print("报表导出完成")


export_report()