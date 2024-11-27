from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SESSION_FILE: str
    SESSION_TYPE: str

    APP_VERSION: str
    DEVICE_MODEL: str
    SYSTEM_VERSION: str
    WORKDIR: str


settings = Settings()
