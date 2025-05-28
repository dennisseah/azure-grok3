from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

from azure_grok3.hosting import container
from azure_grok3.protocols.i_azure_grok3_service import IAzureGrok3Service

svc = container.resolve(IAzureGrok3Service)


def generate(
    system_prompt: str,
) -> str:
    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system_prompt},
    ]
    response = svc.get_client().chat.completions.create(
        model=svc.get_model(),
        messages=messages,
    )
    response_message = response.choices[0].message
    return (
        response_message.content
        if response_message and response_message.content
        else ""
    )


print(generate("Can help to understand Grok3 model"))
