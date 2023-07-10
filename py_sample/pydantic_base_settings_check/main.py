from pydantic import BaseModel, BaseSettings, Field



class Metadata(BaseModel):
    name: str = "name"
    content: str = "meta"


class EnvSettings(BaseSettings):
    metadata: Metadata = Field(Metadata(), env="custom_meta")
    text: str = Field("default", env="custom_text")


def main() -> None:
    env = EnvSettings()
    print(env.metadata)
    print(env.metadata.name)
    print(env.metadata.content)
    print(env.text)
    print(env.dict())
    print("DONE")


if __name__ == "__main__":
    main()
