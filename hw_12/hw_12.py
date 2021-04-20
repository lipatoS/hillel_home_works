import json


def makes_dict():
    with open("HW.json", 'r') as json_file:
        dict_ = json.load(json_file)
        print('Файл загружен')
    return dict_


def dict_sort_types(result_dict):
    employee = result_dict['employee']
    main_dict = {}
    for j in employee:
        first_name = j.get('firstName')
        last_name = j.get('lastName')
        total_name = f"{first_name} {last_name}"
        int_ = []
        string_ = []
        float_ = []
        none_ = []
        bool_ = []
        for k, v in j.items():
            if type(v) == int:
                int_.append(k)
            elif type(v) == str:
                string_.append(k)
            elif type(v) == float:
                float_.append(k)
            elif type(v) is None:
                none_.append(k)
            elif type(v) == bool:
                bool_.append(k)
        dict_types = {'int': int_, 'string': string_, 'float': float_, 'None': none_, 'bool': bool_}
        dict_names = {total_name: dict_types}
        main_dict.update(dict_names)
        result_dict.update({'employee': main_dict})
    print('Словарь отсортирован по типам')
    return result_dict


def save_sorted_dict(result_dict):
    with open('./HW_result.json', 'w') as file:
        json.dump(result_dict, file, indent=1)


def main():
    save_sorted_dict(dict_sort_types(makes_dict()))


main()
