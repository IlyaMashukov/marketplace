from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base, relationship


metadata = MetaData(schema='marketplace')
Base = declarative_base(metadata=metadata)


"""Определение таблиц-связок без указания схемы"""
user_basket = Table(
    'user_basket', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('quantity', Integer, default=1)
)


shop_products = Table(
    'shop_products', Base.metadata,
    Column('shop_id', Integer, ForeignKey('shop.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('stock', Integer, default=0)
)


class User(Base):
    """Класс - модель для таблицы user"""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    basket = relationship("Product", secondary=user_basket, back_populates="users")


class Product(Base):
    """Класс - модель для таблицы product"""
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    price = Column(Float)
    amount = Column(Integer)
    description = Column(String(100))
    users = relationship("User", secondary=user_basket, back_populates="basket")
    shops = relationship("Shop", secondary=shop_products, back_populates="products")


class Shop(Base):
    """Класс - модель для таблицы shops"""
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    products = relationship("Product", secondary=shop_products, back_populates="shops")
