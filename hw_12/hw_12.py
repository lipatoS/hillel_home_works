import json

# json_data = '''{
#     "employee": [
#     {
#       "id": 1,
#       "firstName": "Tom",
#       "lastName": "Cruise",
#       "age": 34,
#       "photo": "cdn2.gossipcenter.com/sites/default/files/imagecac...",
#       "is_active": true,
#       "rewards": null,
#       "salary": 1.3
#     },
#     {
#       "id": 2,
#       "firstName": "Maria",
#       "lastName": "Sharapova",
#       "age": 34,
#       "is_active": false,
#       "rewards": null,
#       "salary": 7.8
#     },
#     {
#       "id": 3,
#       "firstName": "James",
#       "lastName": "Bond",
#       "photo": "georgesjournal.files.wordpress.com/2012/02/007_at_...",
#       "is_active": true,
#       "rewards": null,
#       "salary": 5.6
#     }
#   ]
# }'''
# data = json.loads(json_data)
# with open("my.json", "w") as file:
#     json.dump(data, file, indent=1)
with open('my.json', 'r') as file:
    data = json.load(file)
print(data)