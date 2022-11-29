import logging
import os

from pydantic import BaseSettings, AnyUrl
from functools import lru_cache
"""
    Here, we defined a Settings class with two attributes:

    environment - defines the environment (i.e., dev, stage, prod)
    testing - defines whether or not we're in test mode
    BaseSettings, from pydantic, validates the data so that when we create 
    an instance of Settings, environment and testing will have types of str and bool,
    respectively.

    BaseSettings also automatically reads from environment variables for these 
    config settings. In other words, environment: str = "dev" is equivalent to 
    os.getenv("ENVIRONMENT", "dev").
    
"""


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False
    email: str
    app_name: str
    database_url: AnyUrl = None
    DB_USER : str
    DB_PASSWORD : str
    DB_NAME : str
    DB_HOST : str
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    # class Config:
    #     env_file = ".env"

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()

# class Config:
#     DB_USER = os.getenv("DB_USER", "postgres")
#     DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
#     DB_NAME = os.getenv("DB_NAME", "postgres")
#     DB_HOST = os.getenv("DB_HOST", "localhost")
#     DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"