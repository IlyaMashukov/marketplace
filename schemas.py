from typing import List

from pydantic import BaseModel, constr


class UserBase(BaseModel):
    """Валидация для пользователя"""
    id: int
    name: str
    email: str
    basket: List['ProductBase'] = []


class UserBaseList(BaseModel):
    """Валидация для списка пользователей"""
    users: list[UserBase]


class UserCreate(BaseModel):
    """Валидация для добавления пользователя"""
    name: str
    email: str


class ProductBase(BaseModel):
    """Валидация для продукта"""
    class Config:
        arbitrary_types_allowed = True
    id: int
    title: str
    price: float
    amount: int
    description: constr(max_length=100)
    # users = relationship("User", secondary=user_basket, back_populates="basket")
    # shops = relationship("Shop", secondary=shop_products, back_populates="products")


class ProductBaseList(BaseModel):
    """Валидация для списка продуктов"""
    products: list[ProductBase]


class ProductCreate(BaseModel):
    """Валидация для добавления продукта"""
    title: str
    price: float
    amount: int
    description: constr(max_length=100)
