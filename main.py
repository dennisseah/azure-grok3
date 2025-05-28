from azure_grok3.hosting import container
from azure_grok3.protocols.i_azure_grok3_service import IAzureGrok3Service

svc = container.resolve(IAzureGrok3Service)
print(svc.generate("Can help to understand Grok3 model"))
