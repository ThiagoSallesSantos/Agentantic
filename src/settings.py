## Description: This is the settings file for the application.

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

class APPSettings(BaseModel):
    app_host: str
    app_port: int
    app_debug: bool

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    ) 
    version: str
    application: APPSettings
