import pytest

def reverse(string: str) -> str:
    """
    Возвращает строку в обратном порядке, приведённую к нижнему регистру.
    """
    return string.lower()[::-1]


@pytest.mark.parametrize("original, expected", [
    ('!dlroW olleH', 'hello world!'),
    ('123ABC', 'cba321'),
])

def test_reverse(original, expected):
    assert reverse(original) == expected

# pytest test_reverse.py
