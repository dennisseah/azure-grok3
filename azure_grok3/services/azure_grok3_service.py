from dataclasses import dataclass

from lagom.environment import Env
from openai import AzureOpenAI
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

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

    def generate(
        self,
        system_prompt: str,
    ) -> str:
        messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": system_prompt},
        ]
        response = self.get_client().chat.completions.create(
            model=self.env.azure_grok3_model,
            messages=messages,
        )
        response_message = response.choices[0].message
        return (
            response_message.content
            if response_message and response_message.content
            else ""
        )
