from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = "Intra2004"
    database_username: str = "postgres"
    database_name: str
    secret_key: str = "1234567890podgshjkugdsaafvgllbfdsza"
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file =".env"


settings = Settings()

