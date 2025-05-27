import asyncio

from pydantic import with_config
from sqlalchemy import select

from db_helper import helper_db
from models import User, Base


async def create_tables():
    async with helper_db.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_users():
    async with helper_db.async_session_factory() as session:
        stmt = select(User).order_by(User.name.asc())
        result = await session.execute(stmt)
        users = result.scalars.all()
    return users

async def add_user():
    async with helper_db.async_session_factory() as session:
        try:
            new_user = User(name="Ilya", email="ilya@mail.com")
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)

            return new_user

        except Exception as e:
            # В случае ошибки откатываем транзакцию
            await session.rollback()
            raise e
