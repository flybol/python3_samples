from functools import wraps

def simple_cache(func):
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key in cache_data:
            print("[缓存] 命中缓存")
            return cache_data[key]
        
        print("[缓存] 没有缓存，执行函数")
        result = func(*args, **kwargs)
        cache_data[key] = result
        return result
    
    return wrapper

@simple_cache
def get_user_info(user_id: int):
    print("模拟查询数据库")
    return {
        "user_id": user_id,
        "username": "张三"
    }

print(get_user_info(1))
print(get_user_info(1))