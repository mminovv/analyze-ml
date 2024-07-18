from typing import Optional

from pydantic.v1 import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Base settings
    """
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore',
    )

    # Postgres settings
    POSTGRES_USER: Optional[str]
    POSTGRES_PASSWORD: Optional[str]
    POSTGRES_DB: Optional[str]
    POSTGRES_HOST: Optional[str]
    POSTGRES_PORT: Optional[str]
    SQLALCHEMY_POOL_SIZE: int = 10
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Redis settings
    REDIS_HOST: Optional[str]
    REDIS_PORT: Optional[str]
    REDIS_DB: Optional[str]


    def build_psql_url(  # noqa
        self,
        pg_user,
        pg_password,
        pg_host,
        pg_port,
        pg_db
    ):
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=pg_user,
            password=pg_password,
            host=pg_host,
            port=pg_port,
            path='/{0}'.format(pg_db),
        )

    def build_sync_psql_url(self):
        return PostgresDsn.build(
            scheme='postgresql',
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path='/{0}'.format(self.POSTGRES_DB),
        )

    @property
    def db_url(self):
        return self.build_psql_url(
            pg_user=self.POSTGRES_USER,
            pg_password=self.POSTGRES_PASSWORD,
            pg_host=self.POSTGRES_HOST,
            pg_port=self.POSTGRES_PORT,
            pg_db=self.POSTGRES_DB,
        )


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
