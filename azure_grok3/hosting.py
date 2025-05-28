"""Defines our top level DI container.
Utilizes the Lagom library for dependency injection, see more at:

- https://lagom-di.readthedocs.io/en/latest/
- https://github.com/meadsteve/lagom
"""

import logging

from dotenv import load_dotenv
from lagom import Container, dependency_definition

from azure_grok3.protocols.i_azure_grok3_service import IAzureGrok3Service

load_dotenv(dotenv_path=".env")


container = Container()
"""The top level DI container for our application."""


# Register our dependencies ------------------------------------------------------------


@dependency_definition(container, singleton=True)
def _() -> logging.Logger:
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger("azure_grok3")


@dependency_definition(container, singleton=True)
def grok3() -> IAzureGrok3Service:
    from azure_grok3.services.azure_grok3_service import AzureGrok3Service

    return container[AzureGrok3Service]
