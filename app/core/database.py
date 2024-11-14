from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import POSTGRES_CONFIG

if TYPE_CHECKING:
    from sqlalchemy import URL

class PostgresDB:

    def __init__(self, url: URL):
        self.engine = create_async_engine(url=url)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()

session = PostgresDB(POSTGRES_CONFIG.get_connection_url)
