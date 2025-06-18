import os
from yadisk import YaDisk
from yadisk.exceptions import DirectoryExistsError
from io import BytesIO
from utils.logger import get_log, setup_log
from utils.uploader import build_remote_path, ensure_remote_path_exists, upload_on_disk



setup_log()
logger = get_log(__name__)


def check_token() -> YaDisk | None:
        from dotenv import load_dotenv
        load_dotenv() # получаем переменную окружения 
        yandex_disk_token = os.getenv("yandex_disk_token")

        if not yandex_disk_token:
            logger.error(f"Токен не найден. Проверьте файл .env.")
            return None
        y_disk = YaDisk(token=yandex_disk_token)
        try:
            if not y_disk.check_token():
                logger.error(f"Неверный токен диска.")
                return None
            return y_disk
        except Exception as e:
            logger.error(f"Ошибка при проверке токена: {e}")
            return None


def create_remote_directory(y_disk: YaDisk, remote_dir: str):
    """
    Создаёт папку на Яндекс.Диске, если она ещё не существует.
    """
    try:
        ensure_remote_path_exists(y_disk, remote_dir)
    except Exception as e:
        if "existent directory" not in str(e):
            logger.error(f"Ошибка создания папки {remote_dir}: {e}")


def upload_single_image(y_disk: YaDisk, image_data, remote_path: str):
    """
    Загружает одно изображение на Яндекс.Диск.
    """
    image_data.seek(0)  # Перематываем поток в начало
    upload_on_disk(y_disk, image_data, remote_path)