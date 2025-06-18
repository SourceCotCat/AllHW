from pprint import pprint

def open_file(file: str) -> dict[str, list[dict[str, int | str]]]:
    """
    Открывает указанный .txt-файл и возвращает содержимое в виде словаря.

    :param file: Путь к файлу с расширением '.txt'.
    :type file_path: str
    :return: Словарь, сформированный на основе содержимого файла. 
    """
    cook_book = {}

    with open(file, 'r', encoding='utf-8') as f:
        while True:

            dish_name = f.readline().strip()
            if not dish_name:
                break

            count_ingr = int(f.readline().strip())
            ingredients = []

            for _ in range(count_ingr):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({'ingredient_name' : ingredient_name, 'quantity': int(quantity), 'measure': measure})
            
            cook_book[dish_name] = ingredients

            f.readline()

    return cook_book   

def pretty_print(cook_book: dict[str, list[dict[str, int | str]]]) -> None:
    """
    Функция для красивого форматированного вывода книги рецептов.

    :param cook_book: Словарь, содержащий рецепты блюд.
    :type cook_book: dict
    :return: Ничего не возвращает, только выводит данные на экран.
    """
    print("{")
    for dish, ingredients in cook_book.items():
        print(f"'{dish}': [")
        for ingredient in ingredients:
            print(f"    {ingredient},")
        print(" ],")
    print("}")


def get_shop_list_by_dishes(dishes: list[str], person_count: int) -> tuple[dict[str, dict[str, str | int]], list[str]]: 
    """
    Функция рассчитывает количество ингредиентов для приготовления блюд на указанное количество гостей.

    :param dishes: Список, содержащий названия блюд.
    :type dishes: List[str]
    :return: Кортеж, содержащий словарь с ингредиентами и список отсутствующих блюд.
    """
    cook_lst = {}
    missing_dishes = []

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingr = ingredient['ingredient_name']
                quan = ingredient['quantity'] * person_count
                mea = ingredient['measure']

                if ingr in cook_lst:
                    cook_lst[ingr]['quantity'] += quan
                else:
                    cook_lst[ingr] = {'measure': mea, 'quantity': quan}
        else:
            missing_dishes.append(dish)

    return cook_lst, missing_dishes

cook_book = open_file('recipes.txt')
# pretty_print(cook_book)

res, missing = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(res)

if missing: # поздно увидела, что в задании прописано, что список блюд из cook_book и других быть не может)) но оставимс
    print("\nОтсутствующие блюда:")
    print(", ".join(missing))

