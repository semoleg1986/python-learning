from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Items API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Test API on fastAPI"


settings = Settings()
