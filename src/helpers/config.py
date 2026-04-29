from pydantic_settings import BaseSettings, SettingConfigDict

class settings(BaseSettings):
    APP_NAME:str 
    APP_VERSION:str
    OPEN_API_KEY:str 

    class config:
        env_file = ".env"

def get_settings():
    return settings()