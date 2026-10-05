from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://talenthub:talenthub@db:5432/talenthub"
    redis_url: str = "redis://redis:6379/0"
    hh_api_url: str = "https://api.hh.ru"
    fsp_api_url: str = "https://fsp-russia.com/api"
    parse_interval_minutes: int = 30

    class Config:
        env_prefix = "TH_"
        env_file = ".env"


settings = Settings()
