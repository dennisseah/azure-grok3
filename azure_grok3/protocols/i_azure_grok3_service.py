from typing import Protocol

from openai import AzureOpenAI


class IAzureGrok3Service(Protocol):
    """
    IAzureGrok3Service is a protocol that defines the interface for
    Azure Grok3 service classes. It includes a method to get a
    generative model with specified parameters.
    """

    def get_client(self) -> AzureOpenAI:
        """
        Get client

        :return: An instance of AzureOpenAI.
        """
        ...

    def get_model(self) -> str:
        """
        Get the model name from the environment.

        :return: The model name.
        """
        ...
