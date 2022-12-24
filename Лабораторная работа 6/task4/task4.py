import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(input_file) -> list[dict]:
        with open(input_file) as file_: # открываем
            list_rows = file_.read().split('\n') # разделяем файл
            list_data = [row.split(',') for row in list_rows] # делим строку
            list_dict = [dict(zip(list_data[0], list_data[i])) for i in range(1, len(list_rows))]
        return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# пустая строка