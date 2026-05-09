from functools import wraps


class FakeDBSession:
    def commit(self):
        print("[数据库] 提交事务")

    def rollback(self):
        print("[数据库] 回滚事务")

    def close(self):
        print("[数据库] 关闭连接")


def transactional(func):
    @wraps(func)
    def wrapper(db,*args, **kwargs):
        try:
            result = func(db, *args, **kwargs)
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            print(f"[事务] 发生异常：{e}")
            raise
        finally:
            db.close()

    return wrapper


@transactional
def create_order(db, user_id: int, product_id: int):
    print(f"创建订单：user_id={user_id}, product_id={product_id}")
    print("扣减库存")
    print("生成支付记录")

db = FakeDBSession()
create_order(db,1001, 2002)