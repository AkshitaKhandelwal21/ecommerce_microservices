from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    user_service_url: str

    model_config = SettingsConfigDict(env_file='.env')

    
settings = Settings()