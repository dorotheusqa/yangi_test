from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic.networks import HttpUrl


class UrlSettings(BaseSettings):
    base_url: HttpUrl

    model_config = SettingsConfigDict(env_file=".env")


url_settings = UrlSettings()
