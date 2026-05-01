from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str
    File_Allowed_Types: list[str]
    File_Max_Size: int
    File_Default_Chunk_Size: int 
    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()