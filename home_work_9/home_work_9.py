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


# all()
# The all() function returns True if all elements in the given iterable are true.
# If not, it returns False.
a = {0, 1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(all(a))
print(all(b))

# any()
# The any() function returns True if any element of an iterable is True.
# If not, any() returns False.
a = {0}
print(any(a))
b = {4, 6, 0, 8}
print(any(b))

# enumerate()
# The enumerate() method adds counter to an iterable and returns it (the enumerate object).
set_ = {"milk", "butter", "bread"}
print(list(enumerate(set_)))
print(list(enumerate(set_, 10)))

# The len() function returns the number of items (length) in an object.
# len()
a = {1, 2, 3, 4, 5}
b = {"v", "a", "o", "b", "w", "c"}
print(len(a))
print(len(b))

# max()
# The Python max() function returns the largest item in an iterable.
# It can also be used to find the largest item between two or more parameters.
a = {2, 0, 77}
b = {"aa", "aaa", "aaaaa"}
print(max(a))
print(max(b))

# min()
# The Python min() function returns the smallest item in an iterable.
# It can also be used to find the smallest item between two or more parameters.
a = {2, 0, 77}
b = {"aa", "aaa", "aaaaa"}
print(min(a))
print(min(b))

# sum()
# The sum() function adds the items of an iterable and returns the sum.
a = {1, 2.2, 2.8, -4, 5}
print(sum(a))

# sorted()
# The sorted() function returns a sorted list from the items in an iterable.
a = {5, 88, 2, 35, 6}
b = {"v", "a", "o", "b", "w", "c"}
print(sorted(a))
print(sorted(b))
