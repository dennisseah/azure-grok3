from unittest.mock import MagicMock

from pytest_mock import MockerFixture

from azure_grok3.services.azure_grok3_service import AzureGrok3Service


def test_get_client(mocker: MockerFixture):
    patched_azure_openai = mocker.patch(
        "azure_grok3.services.azure_grok3_service.AzureOpenAI",
        autospec=True,
    )
    svc = AzureGrok3Service(env=MagicMock())
    assert svc.get_client() is not None
    patched_azure_openai.assert_called_once()


def test_tool_calls(mocker: MockerFixture):
    mock_llm_client = MagicMock()

    mock_llm_client.chat.completions.create.return_value.choices = [
        MagicMock(message=MagicMock(content="test output"))
    ]
    svc = AzureGrok3Service(env=MagicMock(), client=mock_llm_client)
    result = svc.generate("Test system prompt")
    assert result == "test output"
