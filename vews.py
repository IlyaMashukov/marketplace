from fastapi import APIRouter, HTTPException

from schemas import UserBase, UserBaseList, UserCreate
from service import get_users, add_new_user

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
