import asyncpg
import os

db_ = os.environ.get("db")


async def create_user(user_id: int):
    db = await asyncpg.connect(db_)
    await db.conn.execute(f"INSERT INTO user (id,balance) VALUES ({user_id}, 0)")
    await db.commit()


async def user_exist(user_id: int):
    db = await asyncpg.connect(db_)
    return await db.fetch(
        f"""
        select exists(select 1 from user where id={user_id})
        """
    )


async def get_balance(user_id: int):
    pass


async def get_bank_balance(user_id: int):
    pass
