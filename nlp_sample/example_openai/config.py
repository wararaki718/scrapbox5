from pydantic import BaseSettings


class OpenAPISettings(BaseSettings):
    openai_api_key: str
    openai_org_id: str
