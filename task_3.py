# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.


import json
import csv


__all__ = ['json_to_csv']


def json_to_csv(file_name: str):
    with open(f'{file_name}.json', 'r') as f_inp:
        data = json.load(f_inp)

    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({'level': level,
                        'name': name,
                        'id': id})

    with open(f'{file_name}.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames=['level',
                                                    'name',
                                                    'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json_to_csv('users')