import json

with open('HW.json', 'r') as file:
    data = json.load(file)

with open("НW_result.json", "w") as json_file:
    json.dump(data, json_file, indent=1)
