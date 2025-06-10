from fastapi import APIRouter, HTTPException

from schemas import UserBase, UserBaseList, UserCreate, ProductBase, ProductBaseList, ProductCreate
from service import get_users, add_new_user, get_products, add_new_product

router = APIRouter(prefix='/users')

@router.get('/all')
async def get_all_users():
    users = await get_users()
    print(f'Вывод пользователей')
    user_base_list = [UserBase(
        id=user.id,
        name=user.name,
        email=user.email
    ) for user in users]
    return UserBaseList(users=user_base_list)


@router.post('/create')
async def create_new_user(user: UserCreate):
    try:
        result = await add_new_user(user.name, user.email)
        if result:
            print(f"Пользователь {user.name} создан")
        return {"message": f"Пользователь {user.name} создан"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


prod_router = APIRouter(prefix='/products')

@prod_router.get('/all')
async def get_all_products():
    products = await get_products()
    print('Вывод списка всех продуктов')
    product_base_list = [
        ProductBase(
            id=product.id,
            title=product.title,
            price=product.price,
            amount=product.amount,
            description=product.description
        ) for product in products]
    return ProductBaseList(products=product_base_list)


@prod_router.post('/create')
async def create_new_product(product: ProductCreate):
    try:
        result = await add_new_product(product.title, product.price, product.amount, product.description)
        if result:
            print(f"Продукт {product.title} создан")
        return {"message": f"Продукт {product.title} создан"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
