import pytest

from bottery.plataform.telegram import TelegramAPI, TelegramUser, mixed_case


# TelegramUser

def test_telegram_user_with_last_name():
    sender = {
        'id': 1,
        'first_name': 'Andrew',
        'last_name': 'Martin',
    }

    user = TelegramUser(sender)
    assert str(user) == 'Andrew Martin (1)'


def test_telegram_user_without_last_name():
    sender = {
        'id': 1,
        'first_name': 'Andrew',
    }

    user = TelegramUser(sender)
    assert str(user) == 'Andrew (1)'


# TelegramAPI

def test_mixed_case():
    assert mixed_case('set_webhook') == 'setWebhook'
    assert mixed_case('get_chat_member') == 'getChatMember'


def test_telegram_api_url():
    token = 123
    api = TelegramAPI(token)
    expected_url = 'https://api.telegram.org/bot123/setWebhook'
    assert api.make_url('set_webhook') == expected_url


def test_telegram_api_method_not_defined():
    api = TelegramAPI('token')
    with pytest.raises(AttributeError):
        api.get_chat_member()
