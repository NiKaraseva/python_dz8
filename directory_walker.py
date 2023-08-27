# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }


import os
import json
import csv
import pickle


__all__ = ['dir_walker']


def get_size(dir_name: str) -> float:
    total_sum = 0
    for root, dirs, files in os.walk(dir_name):
        for f in files:
            full_path = os.path.join(root, f)
            total_sum += os.path.getsize(full_path)
    return total_sum


def dir_walker(dir_name: str):
    res = []
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            full_path = os.path.join(root, name)
            res.append({'name': name,
                        'parent': dirs,
                        'type': 'file',
                        'size': os.path.getsize(full_path)})
        for name in dirs:
            full_path = os.path.join(root, name)
            res.append({'name': name,
                        'parent': root,
                        'type': 'dir',
                        'size': get_size(full_path)})


    with open('dz_8.json', 'w', encoding='utf-8') as f_json:
        json.dump(res, f_json, indent=4)

    with open('dz_8.csv', 'w', newline='') as f_csv:
        csv_write = csv.DictWriter(f_csv, fieldnames=['name',
                                                    'parent',
                                                    'type',
                                                    'size'])
        csv_write.writeheader()
        csv_write.writerows(res)

    with open('dz_8.pickle', 'wb') as f_pickle:
        pickle.dump(res, f_pickle)


if __name__ == '__main__':
    dir_walker('/Users/nikakaraseva/Desktop/GB/PYTHON_new/Seminars/Sem_8')