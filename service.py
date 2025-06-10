from sqlalchemy import select

from db_helper import helper_db
from models import User, Base


async def get_users():
    async with helper_db.async_session_factory() as session:
        stmt = select(User).order_by(User.name.asc())
        result = await session.execute(stmt)
        users = result.scalars().all()
    return users

async def add_new_user(name: str, email: str):
    async with helper_db.async_session_factory() as session:
        new_user = User(
            name=name,
            email=email
        )
        session.add(new_user)
        await session.commit()
        return new_user
