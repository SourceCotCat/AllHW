import re
import pytest

def check_email(email: str) -> bool:
    """
    Проверяет корректность email-адреса по базовым правилам.
    """
    pattern = r"^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email)) and ' ' not in email


@pytest.mark.parametrize("email, expected", [
    ("hello@example.com", True),
    ("user..name@example.com", False),
    ("user@", False),
    ("@example.com", False),
    ("user@.com", False),
    ("user@domain.c", False),
    ("us er@domain.com", False),
    (" em@il.ru", False),
    ("Helloworld@.ru", False),
])

def test_check_email(email, expected):
    assert check_email(email) == expected


# pytest test_email.py