from pydantic import BaseModel, BaseSettings


class OpenAISettings(BaseSettings):
    openai_api_key: str
    openai_org_id: str


class PromptConfig(BaseModel):
    openai_settings: OpenAISettings = OpenAISettings()
    model_name: str = "text-davinci-003"
    temperature: float = 0.6

    def get_config(self) -> dict:
        return {
            "api_key": self.openai_settings.openai_api_key,
            "organization": self.openai_settings.openai_org_id,
            "model_name": self.model_name,
            "temperature": self.temperature
        }
