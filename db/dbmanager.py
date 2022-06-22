from motor.motor_asyncio import AsyncIOMotorClient
import os

db_ = os.environ.get("db")

db = AsyncIOMotorClient(db_)["db"]


async def create_user(user_id: int):
    async with await db.start_session() as s:
        query = {"_id": user_id, "pocket": 0, "bank": 0}
        await db.insert_one(query, session=s)


async def user_exist(user_id: int):
    async with await db.start_session() as s:
        return (
            await db.collection.count_documents({"_id": user_id}, limit=1, session=s)
            != 0
        )


async def get_balance(user_id: int):
    async with await db.start_session() as s:
        return await db.find_one({"_id": user_id}, session=s)["pocket"]


async def get_bank_balance(user_id: int):
    async with await db.start_session() as s:
        return await s.find_one({"_id": user_id})["bank"]
