import json


def main(*args, **kwargs):
    result = {}
    list_ = []
    list_4 = []
    kol = 0
    for i in args[0]:
        list_4.append(i)
        if kol < int(len(kwargs) * 4 / len(kwargs)) - 1:
            kol += 1
            continue
        list_.append(list_4)
        list_4 = []
        kol = 0

    index_ = 0
    for k, v in kwargs.items():
        result[v] = list_[index_]
        index_ += 1
    return result


def load_dict(some_dict, json_path):
    with open(json_path, "w")as les_:
        json.dump(results, les_, indent=1)


if __name__ == '__main__':
    results = main((i for i in range(51, 72)),
                   one="one", two="two", three="three", four="four", five="five")
    load_dict(results, json_path="result.json")
