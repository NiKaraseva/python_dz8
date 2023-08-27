# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

# {
#       level: {
#           id: name,
#           ...
#       },
#       ...
# }


import json


__all__ = ['enter_data']


def unique_id(data: dict, id: str) -> bool:
     for item in data.values():
         if id in item.keys():
             return False
     return True


def enter_data(file_name: str) -> None:
    file_name += ".json"

    while True:
        id = input("id: ")
        name = input("name: ")
        level = input("level: ")

        try:
            with open(file_name, 'r', encoding='utf-8') as fr:
                read_dict: dict = json.load(fr)

        except FileNotFoundError:
            read_dict: dict = {str(i): {} for i in range(1, 8, 1)}

        if unique_id(read_dict, id):
            read_dict[level].update({id: name})
        else:
            continue

        with open(file_name, 'w', encoding='utf-8') as fw:
            json.dump(read_dict, fw, indent=2)


if __name__ == "__main__":
    enter_data(file_name='users')



