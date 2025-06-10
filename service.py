from sqlalchemy import select

from db_helper import helper_db
from models import User, Base, Product


async def get_users():
    """Получение всех пользователей"""
    try:
        async with helper_db.async_session_factory() as session:
            stmt = select(User).order_by(User.name.asc())
            result = await session.execute(stmt)
            users = result.scalars().all()
        return users
    except Exception as e:
        print(f"Ошибка при получении пользователей: {e}")
        return []


async def add_new_user(name: str, email: str):
    """Добавление одного пользователя"""
    async with helper_db.async_session_factory() as session:
        new_user = User(
            name=name,
            email=email
        )
        session.add(new_user)
        await session.commit()
        return new_user


async def get_products():
    """Получение всех продуктов"""
    try:
        async with helper_db.async_session_factory() as session:
            stmt = select(Product).order_by(Product.name.asc())
            result = await session.execute(stmt)
            products = result.scalars().all()
        return products
    except Exception as e:
        print(f"Ошибка при получении продуктов: {e}")
        return []


async def add_new_product(title, price, amount, description):
    """Добавление одного пользователя"""
    async with helper_db.async_session_factory() as session:
        new_product = Product(
            title=title,
            price=price,
            amount=amount,
            description=description
        )
        session.add(new_product)
        await session.commit()
        return new_product
