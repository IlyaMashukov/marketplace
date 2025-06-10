from typing import List

from pydantic import BaseModel, constr

from models import Product


class UserBase(BaseModel):
    """Схема валидации для пользователя"""
    id: int
    name: str
    email: str
    # basket: List['Product'] = []


class UserBaseList(BaseModel):
    """Схема валидации для списка пользователей"""
    users: list[UserBase]


class ProductBase(BaseModel):
    """Схема валидации для продукта"""
    class Config:
        arbitrary_types_allowed = True
    id: int
    title: str
    price: float
    amount: int
    description: constr(max_length=100)
    # users = relationship("User", secondary=user_basket, back_populates="basket")
    # shops = relationship("Shop", secondary=shop_products, back_populates="products")


class UserCreate(BaseModel):
    name: str
    email: str



# class User(UserBase):
#     id: int
#     basket: List['Product'] = []
#
#     class Config:
#         orm_mode = True
