from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from utils.image_processing import json_file
from utils.logger import get_log, setup_log
from utils.downloader import get_breeds
import random
import os

setup_log()
logger = get_log(__name__)


def validation(input_data: str, 
               filter=None, 
               failure="Некорректный ввод. Повторите попытку.", 
               allow_empty=False) -> str:
    """Запрашивает у пользователя входные данные, то тех пор пока не будет введено нужное значение"""
    while True: 
        value = input(input_data).strip()
        if not value:
            if allow_empty:
                return ""
            else:
                logger.warning(f"Значение не может быть пустым.")
            continue
        if filter is None or filter(value):
            return value
        else:
            logger.warning(failure)


def clear_f(json_file: str = "results.json"):
    """ Очищаем папку JSON"""
    choice = validation("Очистить файл results.json? (yes/Enter): ",
                        filter=lambda x: x.strip().lower() in ("", "yes"),
                        failure="Введите yes или enter(для пропуска).",
                        allow_empty=True
                        ).strip().lower()
    
    if choice == "yes":
        # Очищаем JSON
        if os.path.exists(json_file): # проверяем сущ-ие указанного пути
            with open(json_file, "w", encoding="utf-8") as f:
                    f.truncate()
            logger.info(f"Файл '{json_file}' очищен.")
        else:
            logger.warning(f"Файл '{json_file}' не найден.") 
    else:
        logger.info(f"Очистка файла отменена.")


def get_user_input_cnt() -> int | None:
        def validator(valu):
            try: 
                num = int(valu)
                if num <= 0:
                    logger.warning(f"Количество изображений должно быть больше 0.")
                    return False
                return True
            except ValueError:
                if valu.lower() == "all":
                    return True
                else:
                    return False

        def cust_filter(value):
            is_v = validator(value)
            if not is_v and value.isdigit():
                return False
            return is_v

        cnt_input = validation("Введите кол-во изображений для скачивания(или 'all' для всех): ", 
                               filter=cust_filter,
                               failure="Введите целое значение или 'all'.", 
                               ).strip().lower()
        
        if cnt_input == "all":
            return None
 
        return int(cnt_input)


def find_breeds_by_subbreed(subbreed: str, all_breeds: dict[str, list[str]]) -> list[str]:
    """
    Возвращает список основных пород, в которых есть указанная подпорода.
    """
    return [main_breed for main_breed, subs in all_breeds.items() if subbreed in subs]


def choose_breed_from_list(matching_breeds: list[str], subbreed: str) -> str | None:
    """
    Предлагает пользователю выбрать породу из списка, если найдено несколько вариантов.
    """
    print(f"Найдены следующие породы для подпороды '{subbreed}':")
    for i, breed in enumerate(matching_breeds, start=1):
        print(f"{i}. {breed}")

    choice = validation(
        "Выберите номер породы (или введите '-' для случайного выбора): ",
        filter=lambda x: x.isdigit() and 1 <= int(x) <= len(matching_breeds) or x.strip() == "-",
        failure=f"Введите число от 1 до {len(matching_breeds)} или '-'."
    ).strip()

    if choice == '-':
        breed = random.choice(matching_breeds)
        logger.info(f"Случайно выбрана порода '{breed}' для подпороды '{subbreed}'.")
    elif choice.isdigit() and 1 <= int(choice) <= len(matching_breeds):
        breed = matching_breeds[int(choice) - 1]
        logger.info(f"Выбрана порода '{breed}' для подпороды '{subbreed}'.")
    else:
        logger.error("Ошибка выбора.")
        return None

    return breed


def resolve_breed_subbreed(subbreed: str, all_breeds: dict[str, list[str]]) -> str | None:
    
    matching_breeds = find_breeds_by_subbreed(subbreed, all_breeds)

    if not matching_breeds:
        logger.error(f"Подпорода '{subbreed}' не найдена.")
        return None

    if len(matching_breeds) > 1:
        return choose_breed_from_list(matching_breeds, subbreed)
    else:
        breed = matching_breeds[0]
        logger.info(f"Подпорода '{subbreed}' найдена в породе '{breed}'.")
        return breed
    

def get_users_breed_subreed() -> tuple[str | None, list[str] | None, str | None]:
        """
        Получает от пользователя название породы или подпороды с автодополнением и повторным запросом при ошибке.
        Возвращает (breed, subbreeds, subbreed)
        """
        all_br = get_breeds()
        breeds_list = list(all_br.keys())
        subbreeds_list = list({sub for subs in all_br.values() for sub in subs})

        breed_completer = WordCompleter(breeds_list, ignore_case=True)
        subbreed_completer = WordCompleter(subbreeds_list, ignore_case=True)

        while True:
            breed_input = prompt(
                f"Введите породу: \n'-' если знаете только подпороду \n'?' если необходима справка \n",
                completer=breed_completer,
                complete_while_typing=True
            ).strip().lower()

            if breed_input == "?":
                print("\nДоступные породы:")
                for breed in sorted(breeds_list):
                    print(f" - {breed}")
                print()
                continue

            elif breed_input == "-":
                while True:
                    subbreed_input = prompt(
                        f"Введите подпороду: \n'?' если необходима справка\n",
                        completer=subbreed_completer,
                        complete_while_typing=True
                    ).strip().lower()

                    if subbreed_input == "?":
                        print("\nДоступные подпороды:")
                        for subbreed in sorted(subbreeds_list):
                            print(f" - {subbreed}")
                        print()
                        continue

                    if not subbreed_input:
                        logger.warning("Название подпороды не может быть пустым.")
                        continue

                    if subbreed_input not in subbreeds_list:
                        logger.warning(f"Подпорода '{subbreed_input}' не найдена.")
                        continue

                    breed = resolve_breed_subbreed(subbreed_input, all_br)
                    if not breed:
                        logger.error("Не удалось определить породу для этой подпороды.")
                        continue

                    return breed, None, subbreed_input

            else:
                # Проверяем корректность породы
                if breed_input not in breeds_list:
                    logger.warning(f"Порода '{breed_input}' не найдена.")
                    continue

                # Получаем список подпород
                subbreeds = all_br.get(breed_input, [])

                # Если есть подпороды — спрашиваем, какую использовать
                if subbreeds:
                    choice = validation(
                        f"Хотите выбрать конкретную подпороду? ({', '.join(subbreeds)}) или введите 'all': ",
                        filter=lambda x: x.strip().lower() in [s.lower() for s in subbreeds + ["all"]],
                        failure=f"Введите одну из подпород или 'all'.",
                        allow_empty=False
                    ).strip().lower()

                    if choice == "all":
                        return breed_input, subbreeds, None
                    else:
                        return breed_input, None, choice
                else:
                    # Нет подпород — просто возвращаем породу
                    return breed_input, None, None
    