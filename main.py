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


user_input = ""

while user_input.lower() != "exit":
    user_input = input("Enter a system prompt (or type 'exit' to quit): ")
    if user_input.lower() != "exit":
        print("Generating response...")
        print(generate(user_input))
