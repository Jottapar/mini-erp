from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #APP
    PROYECT_NAME: str
    VERSION: str
    API_V1_STR: str

    ##DB
    SERVER_HOST: str
    USER: str
    PASSWORD: str
    DB_NAME: str
    PORT: int

    @property
    def database_url(self):
        return f'postgresql:// {self.USER}:{self.PASSWORD}@{self.SERVER_HOST}:{self.PORT}/{self.DB_NAME}'

    model_config= SettingsConfigDict(search_file='.env')

settings = Settings()