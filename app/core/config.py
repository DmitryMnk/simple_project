from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL
from pydantic import ValidationError

class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore')
    user: str
    password: str
    host: str
    port: int
    name: str
    driver: str = 'postgresql+asyncpg'

    def get_connection_url(self) -> URL:
        return URL.create(
            drivername=self.driver,
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name
        )

    def get_connection_string(self) -> str:
        return f'{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'


class Settings(BaseSettings):
    pass

try:
    POSTGRES_CONFIG = PostgresSettings(_env_file='.env', _env_prefix='POSTGRES_')  # type: ignore
except ValidationError:
    ALEMBIC_POSTGRES_CONFIG = PostgresSettings(_env_file='.migration.env', _env_prefix='DB_')  # type: ignore

settings = Settings()
