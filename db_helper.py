from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db_config import settings_db


class DataBaseHelper:
    """Создание движка для работы с базой данных"""
    def __init__(self, url):
        self.async_engine = create_async_engine(url=url, echo=True)
        self.async_session_factory = sessionmaker(
            bind=self.async_engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )


helper_db = DataBaseHelper(url=settings_db.database_url)
