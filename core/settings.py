# Pydantic Settings
from pydantic_settings import BaseSettings, SettingsConfigDict


# Settings
class Settings(BaseSettings):
    base_url: str = ""
    bot_token: str = ""

    model_config = SettingsConfigDict(env_file=".env")


# Run settings
settings = Settings()
