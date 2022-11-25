import logging

from pydantic import BaseSettings
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

    class Config:
        env_file = ".env"

def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()