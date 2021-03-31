# add()
# Добавляет элемент во множество.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.add(88)
print(a)

# clear()
# Удаляет все элементы из множества.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.clear()
print(a)

# copy()
# Возвращает копию множества.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.copy()
print(a)

# discard()
# Удаляет элемент из множества, если он содержится в нем.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.discard(1)
print(a)

# isdisjoint()
# Возвращает значение True, если два множества имеют нулевое пересечение.

a = {1, 2, 3, 4, 5}
b = {6, 7, 8}
print(a)
print(b)
print(a.isdisjoint(b))

# pop()
# Удаляет и возвращает произвольный элемент множество.
# Выдает KeyError, если множество пусто.

a = {1, 2, 3, 4, 5}
b = {6, 7, 8}
print(a)
print(b)
a.pop()
print(a)

# remove()
# Удаляет элемент из набора.
# Если элемент не является членом множества, выдает KeyError.

a = {1, 2, 3, 4, 5}
b = {6, 7, 8}
print(a)
print(b)
a.remove(5)
print(a)

# A.union(B)
# Возвращает множество, являющееся объединением множеств A и B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
print(a | b)
print(a.union(b))

# A.update(B)
# Добавляет в множество A все элементы из множества B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.update({11, 12, 13})
print(a)

# A.intersection(B)
# Возвращает множество, являющееся пересечением множеств A и B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
print(a.intersection(b))

# A.intersection_update(B)
# Оставляет в множестве A только те элементы, которые есть в множестве B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.intersection_update(b)
print(a)

# A.difference(B)
# Возвращает разность множеств A и B (элементы, входящие в A, но не входящие в B).

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
print(a.difference(b))

# A.difference_update(B)
# Удаляет из множества A все элементы, входящие в B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.difference_update(b)
print(a)

# A.symmetric_difference(B)
# Возвращает симметрическую разность множеств A и B
# (элементы, входящие в A или в B, но не в оба из них одновременно).

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
print(a.symmetric_difference(b))

# A.symmetric_difference_update(B)
# Записывает в A симметрическую разность множеств A и B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
a.symmetric_difference_update(b)
print(a)

# A.issubset(B)
# Возвращает true, если A является подмножеством B.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 2, 3, 4, 5, 6, 7, 8}
print(a)
print(b)
print(c)
print(a.issubset(b))
print(a.issubset(c))

# A.issuperset(B)
# Возвращает true, если B является подмножеством A.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 2, 3, 4, 5, 6, 7, 8}
print(a)
print(b)
print(c)
print(a.issuperset(b))
print(b.issubset(c))
