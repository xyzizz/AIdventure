from dataclasses import dataclass
import os

from dotenv import load_dotenv
import os

load_dotenv(
    dotenv_path="./.env"
)


@dataclass
class Config:
    deployment_name: str
    model: str
    azure_api_key: str
    azure_api_base: str
    azure_openai_api_ver: str


def load_config() -> Config:
    # Load configuration from environment variables
    deployment_name = os.getenv("DEPLOYMENT_NAME")
    model = os.getenv("MODEL")
    azure_api_key = os.getenv("AZURE_API_KEY")
    azure_api_base = os.getenv("AZURE_API_BASE")
    azure_openai_api_ver = os.getenv("AZURE_OPENAI_API_VER")

    return Config(
        deployment_name=deployment_name,
        model=model,
        azure_api_key=azure_api_key,
        azure_api_base=azure_api_base,
        azure_openai_api_ver=azure_openai_api_ver,
    )


config = load_config()


def main():
    print(config)


if __name__ == "__main__":
    main()
