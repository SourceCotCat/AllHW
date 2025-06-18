from utils.user_input import get_user_input_cnt, get_users_breed_subreed, clear_f
from utils.yadisk_integration import check_token
from utils.image_processing import proc_image
import os

json_file = os.path.join(os.path.dirname(__file__), "results.json")

def main():
    """ 
    очищаем файл 'results.json в случае необходимости.
    Получаем от пользователя кол-во изображений и название породы(подпороды).
    Проверяем наличие яндекс токена.
    Получаем список пород(подпород) с Api.
    Загружаем изображения на диск.
    Сохраняем информацию в Json.

    Returns:
        None
    """ 
    clear_f(json_file) 
    cnt = get_user_input_cnt()
    breed, subbreeds, subbreed = get_users_breed_subreed()
    if not breed and not subbreed:
        return
    y_disk = check_token()
    if not y_disk:
        return
    proc_image(breed, subbreeds, subbreed, cnt, y_disk)

if __name__ == "__main__":
    main()


