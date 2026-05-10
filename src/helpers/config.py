from pydantic_settings import BaseSettings, SettingsConfigDict
import os

# Get the absolute path to the .env file relative to this config.py file
ENV_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str

    File_Allowed_Types: list[str]
    File_Max_Size: int
    File_Default_Chunk_Size: int 

    MongoDB_URI: str
    MongoDB_Database: str
    
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH
    )


def get_settings():
    return Settings()