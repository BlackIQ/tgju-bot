# Libs
from pydantic_settings import BaseSettings, SettingsConfigDict  # Pydantic Settings


# Settings
class Settings(BaseSettings):
    base_url: str = ""
    bot_token: str = ""

    model_config = SettingsConfigDict(env_file=".env")


# Run settings
settings = Settings()
