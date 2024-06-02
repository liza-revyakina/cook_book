# Чтение по файлу и добавление построчно в список рецептов
with open("recipes.txt", encoding='utf-8') as file:
    recipes = []
    for line in file:
        recipes.append(line)


# Формирование подсписков по рецептам
def split_on(dish, delimiter="\n"):
    splitted = [[]]
    for item in dish:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted


def cook_dict(recipies_list):
    recipies_list = split_on(recipies_list)
    cook_book = {}
    for el, dish in enumerate(recipies_list):
        # Обрезание лишних символов
        for i, each in enumerate(dish):
            ingredient = each.strip()
            recipies_list[el][i] = ingredient
            # Создание словаря для каждого ингридиента
            if i > 1:
                recipies_list[el][i] = recipies_list[el][i].split(" | ")
                recipies_list[el][i] = {"ingredient name": dish[i][0],
                                        "quantity": int(dish[i][1]),
                                        "measure": dish[i][2]}
        # Добавление в словарь каждого рецепта
        cook_book[dish[0]] = dish[2::]
    return cook_book


# Создание списка покупок по внесенным рецептам и кол-ву порций
def get_shop_list_by_dishes(dishes, person_count):
    copy_dict = cook_dict(recipes)
    shop_list = {}
    # Для каждого из внесенных рецептов
    for each in dishes:
        ingredients = copy_dict.get(each)
        # Для каждого ингредиента из рецепта увеличение кол-ва, кратное числу порций
        for ingr_dict in ingredients:
            product_dict = {'measure': ingr_dict.get('measure'), 'quantity': ingr_dict.get('quantity') * person_count}
            # Для повторяющихся продуктов: сложение кол-ва добавляемого продукта с имеющимся
            if ingr_dict.get('ingredient name') in shop_list:
                shop_list[ingr_dict.get('ingredient name')] = (
                    product_dict.update({'quantity': product_dict.get('quantity') +
                                        shop_list.get((ingr_dict.get('ingredient name')).get('quantity'))})
                )
            shop_list[ingr_dict.get('ingredient name')] = product_dict
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))