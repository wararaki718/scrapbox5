import openai

from config import OpenAPISettings


def get_model(env: OpenAPISettings) -> openai.Model:
    openai.organization = env.openai_org_id
    openai.api_key = env.openai_api_key
    return openai.Model


def main() -> None:
    env = OpenAPISettings()

    model = get_model(env)

    print(model.list())
    print("DONE")


if __name__ == "__main__":
    main()
