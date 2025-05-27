from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSettings(BaseSettings):
    """Настройки подключения к базе данных"""
    DB_HOST: str = ''
    DB_PORT: int = 5432
    DB_USER: str = ''
    DB_PASS: str = ''
    DB_NAME: str = ''


    @property
    def database_url(self):
        """Формирование строки адреса для подключения к базе данных"""
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    model_config = SettingsConfigDict(env_file='.env')

settings_db = DataBaseSettings()
