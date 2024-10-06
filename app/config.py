from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """config settings for the application"""

    APP_NAME: str = "FastAPI CRUD"
    FASTAPI_ENV: str = "dev"
    DATABASE_URI: str = ""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()
