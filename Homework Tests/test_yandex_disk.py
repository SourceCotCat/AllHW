import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv()  # получаем переменную окружения


TOKEN = os.getenv("yandex_disk_token")
API_BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'  
TEST_FOLDER_PATH = 'test_folder_api'
HEADERS = {
    'Authorization': f'OAuth {TOKEN}'
}


def test_create_folder():
    """Тест: успешное создание папки"""
    params = {'path': TEST_FOLDER_PATH}
    response = requests.put(API_BASE_URL, headers=HEADERS, params=params)

    assert response.status_code == 201, f"Код ответа не равен 201, получен: {response.status_code}"

    # Проверяем наличие папки в корневом каталоге
    response_get = requests.get(API_BASE_URL, headers=HEADERS, params={'path': '/'})
    assert response_get.status_code == 200

    items = response_get.json()['_embedded']['items']
    folder_names = [item['name'] for item in items if item['type'] == 'dir']
    assert TEST_FOLDER_PATH in folder_names, f"Папка '{TEST_FOLDER_PATH}' не найдена в списке файлов. Найдены папки: {folder_names}"


def test_create_folder_missing_token():
    """Тест: отсутствие токена -> ошибка 401"""
    bad_headers = {}
    params = {'path': 'test_folder_no_token'}
    response = requests.put(API_BASE_URL, headers=bad_headers, params=params)

    assert response.status_code == 401, f"Ожидается код ошибки 401 при отсутствии токена, получен: {response.status_code}"

    # Проверяем структуру ответа с ошибкой
    response_json = response.json()
    assert 'error' in response_json, f"В ответе должен быть ключ 'error', получен ответ: {response_json}"


def test_create_folder_invalid_token():
    """Тест: неверный токен -> ошибка 401"""
    bad_headers = {'Authorization': 'OAuth invalid_token'}
    params = {'path': 'test_folder_invalid_token'}
    response = requests.put(API_BASE_URL, headers=bad_headers, params=params)

    assert response.status_code == 401, f"Ожидается код ошибки 401 при неверном токене, получен: {response.status_code}"

    response_json = response.json()
    assert 'error' in response_json, f"В ответе должен быть ключ 'error', получен ответ: {response_json}"


def test_create_folder_missing_path():
    """Тест: отсутствие параметра path -> ошибка 400"""
    response = requests.put(API_BASE_URL, headers=HEADERS)
    assert response.status_code == 400, f"Ожидается код ошибки 400 при отсутствии path, получен: {response.status_code}"

    response_json = response.json()
    assert 'error' in response_json, f"В ответе должен быть ключ 'error', получен ответ: {response_json}"


def test_create_folder_already_exists():
    """Тест: создание папки, которая уже существует -> ошибка 409"""
    params = {'path': TEST_FOLDER_PATH}

    # Создаем папку первый раз
    response1 = requests.put(API_BASE_URL, headers=HEADERS, params=params)
    assert response1.status_code == 201, "Первое создание папки должно быть успешным"

    # Пытаемся создать ту же папку второй раз
    response2 = requests.put(API_BASE_URL, headers=HEADERS, params=params)
    assert response2.status_code == 409, f"Ожидается код ошибки 409 при повторном создании папки, получен: {response2.status_code}"

    response_json = response2.json()
    assert 'error' in response_json, f"В ответе должен быть ключ 'error', получен ответ: {response_json}"


@pytest.fixture(autouse=True)
def cleanup_folder():
    """Фикстура: удаляет тестовую папку после каждого теста"""
    yield
    # Удаляем папку после теста, если она существует
    params = {'path': TEST_FOLDER_PATH, 'permanently': True}
    try:
        requests.delete(API_BASE_URL, headers=HEADERS, params=params)
    except:
        pass  # Игнорируем ошибки при удалении (папка может не существовать)


# py -m pytest test_yandex_disk.py -v