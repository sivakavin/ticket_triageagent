from functools import lru_cache
from pydantic import Field,SecretStr
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_prefix= "AGENT_",
        extra="ignore",
    )

    # App
    app_name:str = "triage_agent"
    environment:str = "dev"  # dev|stage|prod
    log_level:str = "INFO"

    # LLM
    llm_provider:str = "groq"
    llm_model:str = "meta-llama/llama-prompt-guard-2-22m"
    llm_temperature:float = Field(default=0.0,ge=0,le=2)
    llm_max_token:int = 1024
    llm_api_key:SecretStr

    # Agent behaviour
    max_iterations:int=5

@lru_cache
def get_settings() -> Settings:
    return Settings()