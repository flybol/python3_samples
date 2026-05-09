from functools import wraps


current_user = {
    "username": "zhangsan",
    "roles": ["user", "admin","user:delete"]
}


def require_role(role: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role not in current_user["roles"]:
                raise PermissionError(f"没有权限，需要角色：{role}")

            print(f"[权限] 用户 {current_user['username']} 权限校验通过")
            return func(*args, **kwargs)

        return wrapper

    return decorator

@require_role("admin")
def delete_user(user_id: int):
    print(f"删除用户：{user_id}")


delete_user(1001)