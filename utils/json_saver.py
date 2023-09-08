import json
import os


def write_to_json_file(output_file, data):
    """Метод записывает в файл output_file с JSON-данные data,
    сохраняя имеющиеся в нем данные"""
    try:
        with open(output_file, "a") as json_file:
            # Проверяем файл на содержимое. Размер = 0 значит пустой
            if os.stat(output_file).st_size == 0:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            else:  # Иначе считываем из файла данные
                with open(output_file) as json_file:
                    data_list = json.load(json_file)
                # Добавляем к ним новые
                data_list.append(data)
                # И записываем всё вместе в файл
                with open(output_file, "w") as json_file:
                    json.dump(data_list, json_file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('\nНе найден файл с данными\n')
