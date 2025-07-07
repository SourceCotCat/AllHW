import pytest

def check_age(age: int) -> str:
    """Проверяет возраст и возвращает сообщение о доступе."""
    if age >= 18:
        return 'Доступ разрешён'
    else:
        return 'Доступ запрещён'

def main():
    auth = check_age(10)
    print('Возраст 100:', auth)

    auth = check_age(20)
    print('Возраст 20:', auth)


@pytest.mark.parametrize("age, expected", [
    (10, "Доступ запрещён"),
    (0, "Доступ запрещён"),
    (17, "Доступ запрещён"),
    (18, "Доступ разрешён"),
    (100, "Доступ разрешён")
])

def test_check_age(age, expected):  
    result = check_age(age)
    assert result == expected, f"Для возраста {age} ожидалось '{expected}', но получено '{result}'"


if __name__ == '__main__':
    main()

# pytest test_age.py