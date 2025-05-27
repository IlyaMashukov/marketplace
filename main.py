import asyncio

import uvicorn
from fastapi import FastAPI

from service import create_tables, get_users, add_user

# app = FastAPI()


# asyncio.run(create_tables())
asyncio.run(add_user())
asyncio.run(get_users())


# if __name__ == "__main__":
#     uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
