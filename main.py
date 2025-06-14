import uvicorn
from fastapi import FastAPI

from vews import router, prod_router

app = FastAPI()
app.include_router(router, tags=['users'])
app.include_router(prod_router, tags=['products'])


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
