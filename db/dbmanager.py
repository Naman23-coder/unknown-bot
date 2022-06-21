import asyncpg
import os


class DBmanager:
    def __init__(self) -> None:
        self.db = os.environ.get('db')

    async def get_db(self):
        return await asyncpg.connect(self.db)

    async def create_user(self, user_id: int):
        await self.get_db.conn.execute(f"INSERT INTO user (id,balance) VALUES ({user_id}, 0)")
        await self.get_db().execute()

    async def user_exist(self, user_id: int):
        return self.get_db().fetch(f"""
        select exists(select 1 from user where id={user_id})
        """)
