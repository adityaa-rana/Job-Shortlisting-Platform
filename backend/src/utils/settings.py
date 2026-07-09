# used for reading env variables
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
    DB_CONNECTION:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_TIME:int
    GEMINI_API_KEY: str

# object to retrieve and validate env variable
settings=Settings()
