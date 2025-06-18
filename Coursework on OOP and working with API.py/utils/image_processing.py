import json
from tqdm import tqdm
from yadisk import YaDisk
from utils.logger import get_log, setup_log
from utils.downloader import get_image, download_image
from utils.uploader import build_remote_path
from utils.yadisk_integration import create_remote_directory, upload_single_image

setup_log()
logger = get_log(__name__)


json_file = "results.json"


def process_image(url: str, breed: str) -> tuple | None:
    """
    Скачивает изображение по URL и возвращает имя файла и данные.
    """
    result = download_image(url, breed)
    if result is None:
        return None
    file_name, image_data = result
    return file_name, image_data



def save_metadata(data: list[dict]):
    """
    Сохраняет список данных о файлах в JSON-файл.
    """
    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"JSON успешно сохранён: {json_file}")
    except IOError as e:
        logger.error(f"Ошибка ввода-вывода при сохранении JSON: {e}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка при сохранении JSON: {e}")

def proc_image(breed: str, subbreeds: list[str] | None, subbreed: str | None, cnt: int | None, y_disk: YaDisk):
    
    res = []

    if subbreed:
        breed_sub = [f"{breed}/{subbreed}"]
    else:
        breed_sub = [f"{breed}/{s}" for s in subbreeds] if subbreeds else [breed]

    for bre in breed_sub:
        main_breed, *sub_part = bre.split("/")
        sub = sub_part[0] if sub_part else None

        image_urls = get_image(main_breed, sub)
        if not image_urls:
            logger.warning(f"Изображения для {bre} не найдены.")
            continue

        if cnt:
            image_urls = image_urls[:cnt]

        remote_dir = build_remote_path(main_breed, sub)
        create_remote_directory(y_disk, remote_dir)

        for url in tqdm(image_urls, desc=f"Скачивание {bre}"):
            downloaded = process_image(url, main_breed)
            if downloaded is None:
                continue

            file_name, image_data = downloaded
            remote_path = f"{remote_dir}/{file_name}"

            upload_single_image(y_disk, image_data, remote_path)

            res.append({
                 "file_name": file_name,
                 "breed": main_breed,
                 "subbreed": sub,
                 "url": url
             })

    save_metadata(res)