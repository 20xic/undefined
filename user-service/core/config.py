from pydantic import BaseModel
from pydantic_settings import BaseSettings,SettingsConfigDict

class RunConfig(BaseModel):
    host:str = "localhost"
    port:int = 10990

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template",".env"),
        case_sensitive = False,
        env_nested_delimiter="__",
        env_prefix="USER_SERVICE_CONFIG__",
        extra = "ignore"
    )
    run:RunConfig = RunConfig()


settings = Settings()
