# Задача 2
# Дано три множества
# Одним действием (одной строкой) виполнить intersection єтих множеств

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}
# sets_ = set.intersection(set1, set2, set3)
# print(sets_)

# Задача 3
# Дано три множества
# Одним действием (одной строкой) виполнить difference єтих множеств

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}
# sets_ = set.difference(set1, set2, set3)
# print(sets_)

# Задача 4
# Дано три множества
# Одним действием (одной строкой) виполнить union єтих множеств

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}
# sets_ = set.union(set1, set2, set3)
# print(sets_)

# Задача 5
# Добавить список элементов к заданному набору

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red"]
# sampleSet.update(sampleList)
# print(sampleSet)

# Задача 6
# Вернуть новый набор идентичных предметов из заданных двух наборов

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# sets_ = set.intersection(set1, set2)
# print(sets_)

# Задача 7
# Возвращает новый набор со всеми элементами из обоих наборов, удаляя дубликаты.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# sets_ = set.union(set1, set2)
# print(sets_)

# Задача 8
# Учитывая два набора Python, обновите первый набор элементами,
# которые существуют только в первом наборе, но не во втором наборе.

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# print(set1)
# set1.update(set2)
# print(set1)

# Задача 9
# Удалите єлементи 10, 20, 30 из следующего набора

# set1 = {10, 20, 30, 40, 50}
# set1.remove(10)
# set1.discard(20)
# set1.remove(30)
# print(set1)

# Задача 11
# Проверьте, есть ли в двух наборах какие-либо общие элементы. Если да, отобразите общие элементы.

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# sets_ = set.intersection(set1, set2)
# print(sets_)

# Задача 12
# Обновите набор 1, добавив элементы из набора 2

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# print(set1)
# set1.update(set2)
# print(set1)

# Задача 13
# Удалите элементы из set1, которые не являются общими для set1 и set2

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1)
# set1.intersection_update(set2)
# print(set1)

# Задача 14
# Используя Все полученние знания по всем типам данних виполнить рефакторинг кода задачи с сложним списком из лекции 6
# Код уменьшить до минимального количества строк
list_ = [
    [1, None, 2, 3, 4 + 5j, 6],
    [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1],
    ['1', '2', '3.6', None, '4+5.7j', '6']
]
print(f"list_: {list_}")
for m in range(0, len(list_)):
    int_c = 0
    float_c = 0
    str_c = 0
    for i in list_[m]:
        if type(i) == int:
            int_c += 1
        elif type(i) == float:
            float_c += 1
        elif type(i) == str:
            str_c += 1
    if float_c < int_c > str_c:
        j = 0
        while j < len(list_[m]):
            if type(list_[m][j]) == int:
                j += 1
                continue
            else:
                del list_[m][j]
                j -= 1
            j += 1
    elif int_c < float_c > str_c:
        j = 0
        while j < len(list_[m]):
            if type(list_[m][j]) == float:
                j += 1
                continue
            else:
                del list_[m][j]
                j -= 1
            j += 1
    elif float_c < str_c > int_c:
        j = 0
        while j < len(list_[m]):
            if type(list_[m][j]) == str:
                j += 1
                continue
            else:
                del list_[m][j]
                j -= 1
            j += 1

list_ = list_[0] + list_[1] + list_[2]
list_new = [*list_]
print(f"list_new: {list_new}")
list_1 = [*list_]
list_2 = [*list_]
list_3 = [*list_]

for i in list_1:
    j = 0
    while j < len(list_1):
        if type(list_1[j]) == int:
            j += 1
            continue
        else:
            del list_1[j]
            j -= 1
        j += 1
if len(list_1) == 0:
    print("В списке 'int_list' типа данных 'int' нет")
else:
    print(f"int_list: {list_1}")
for i in list_2:
    j = 0
    while j < len(list_2):
        if type(list_2[j]) == float:
            j += 1
            continue
        else:
            del list_2[j]
            j -= 1
        j += 1
if len(list_2) == 0:
    print("В списке 'int_float' типа данных 'float' нет")
else:
    print(f"int_list: {list_2}")
for i in list_3:
    j = 0
    while j < len(list_3):
        if type(list_3[j]) == str:
            j += 1
            continue
        else:
            del list_3[j]
            j -= 1
        j += 1
if len(list_3) == 0:
    print("В списке 'int_str' типа данных 'str' нет")
else:
    print(f"int_list: {list_3}")
