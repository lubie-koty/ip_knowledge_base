from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    knowledge_base_filename: str = "example.json"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
