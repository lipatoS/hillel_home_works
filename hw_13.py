import json


def main():
    def some_func(*args, **kwargs):
        result = {}
        list_ = []
        list_4 = []
        kol = 0
        for i in args:
            list_4.append(i)
            if kol < int(len(args) / len(kwargs)) - 1:
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
        try:
            with open(json_path, "r")as les_:
                data = json.load(les_)
        except FileNotFoundError:
            with open(json_path, "w")as les_:
                json.dump(results, les_, indent=1)
        else:
            data.update(results)
            with open(json_path, "w") as les_:
                json.dump(data, les_, indent=1)

    results = some_func(51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
                        one="one", two="two", three="three", four="four", five="five")

    load_dict(results, json_path="result.json")


if __name__ == "__main__":
    main()
