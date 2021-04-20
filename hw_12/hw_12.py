import json


def make_dict():
    with open("HW.json", 'r') as json_data:
        dic_d = json.load(json_data)
    print('Файл загружен.')
    return dic_d


def dict_sort_by_type(dic_d):
    employee = dic_d['employee']
    my_dict4 = {}
    for person in employee:
        first_name = person.get('firstName')
        last_name = person.get('lastName')
        fio = f"{first_name} {last_name}"
        ints = []
        strings = []
        floats = []
        nons = []
        bool_ = []
        for pers_key, pers_value in person.items():
            if type(pers_value) is int:
                ints.append(pers_value)
            elif type(pers_value) is str:
                strings.append(pers_value)
            elif type(pers_value) is float:
                floats.append(pers_value)
            elif type(pers_value) is None:
                nons.append(pers_value)
            elif type(pers_value) is bool:
                bool_.append(pers_value)
        my_dict2 = {'int': ints, 'string': strings, 'float': floats, 'None': nons, 'bool': bool_}
        my_dict3 = {fio: my_dict2}
        my_dict4.update(my_dict3)
    dic_d.update({'employee': my_dict4})
    print('Словарь отсортирован по типам.')
    return dic_d


def save_sorted_dict(dic_d):
    with open('HW_result.json', 'w') as file:
        json.dump(dic_d, file, indent=1)


def main():
    save_sorted_dict(dict_sort_by_type(make_dict()))


main()
