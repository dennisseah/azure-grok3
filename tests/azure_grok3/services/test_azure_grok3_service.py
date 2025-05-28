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


def test_get_model(mocker: MockerFixture):
    mock_env = MagicMock()
    mock_env.azure_grok3_model = "grok3-model"
    svc = AzureGrok3Service(env=mock_env, client=MagicMock())
    assert svc.get_client() is not None
    model = svc.get_model()
    assert model == "grok3-model"
