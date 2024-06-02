import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Setting(BaseSettings):
    bot_token: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8"
    )


config = Setting()