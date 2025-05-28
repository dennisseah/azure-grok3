from dataclasses import dataclass

from lagom.environment import Env
from openai import AzureOpenAI

from azure_grok3.protocols.i_azure_grok3_service import IAzureGrok3Service


class AzureGrok3ServiceEnv(Env):
    """
    Environment variables for Azure OpenAI Service.
    """

    azure_grok3_endpoint: str
    azure_grok3_api_version: str
    azure_grok3_model: str
    azure_grok3_api_key: str


@dataclass
class AzureGrok3Service(IAzureGrok3Service):
    env: AzureGrok3ServiceEnv
    client: AzureOpenAI | None = None

    def get_client(self) -> AzureOpenAI:
        if self.client is not None:
            return self.client

        self.client = AzureOpenAI(
            azure_endpoint=self.env.azure_grok3_endpoint,
            api_version=self.env.azure_grok3_api_version,
            api_key=self.env.azure_grok3_api_key,
        )
        return self.client

    def get_model(self) -> str:
        return self.env.azure_grok3_model
