# 1. Define the id of next variables:
# int_a = 55
# str_b = 'cursor'
# set_c = {1, 2, 3}
# lst_d = [1, 2, 3]
# dict_e = {'a': 1, 'b': 2, 'c': 3}

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
d = [4, 5]
lst_d.append(d)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.
if isinstance(int_a, int):
    print('is Int')
if isinstance(int_a, str):
    print('is str')
if isinstance(int_a, set):
    print('is set')
if isinstance(int_a, list):
    print('is list')
if isinstance(int_a, list):
    print('is dict')

if isinstance(str_b, int):
    print('is Int')
if isinstance(str_b, str):
    print('is str')
if isinstance(str_b, set):
    print('is set')
if isinstance(str_b, list):
    print('is list')
if isinstance(str_b, list):
    print('is dict')

if isinstance(set_c, int):
    print('is Int')
if isinstance(set_c, str):
    print('is str')
if isinstance(set_c, set):
    print('is set')
if isinstance(set_c, list):
    print('is list')
if isinstance(set_c, list):
    print('is dict')

if isinstance(lst_d, int):
    print('is Int')
if isinstance(lst_d, str):
    print('is str')
if isinstance(lst_d, set):
    print('is set')
if isinstance(lst_d, list):
    print('is list')
if isinstance(lst_d, list):
    print('is dict')

if isinstance(dict_e, int):
    print('is Int')
if isinstance(dict_e, str):
    print('is str')
if isinstance(dict_e, set):
    print('is set')
if isinstance(dict_e, list):
    print('is list')
if isinstance(dict_e, list):
    print('is dict')


# String formatting:
# Replace the placeholders with a value:
# 5. With .format and curly braces {}
apples = 3
peaches = 5
print("Anna has {} apples and {} peaches.".format(apples, peaches))

# 6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(3, 5))

# 7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=3, peaches=5))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {0:3} peaches.".format('3', '5'))

# 9. With f-strings and variables
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator
print("Anna has %d apples and %d peaches." % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
print(f"Anna has {dict_e ['a']} apples and {dict_e ['b']} peaches.")

# Comprehensions:
# 12. Convert (1) to list comprehension
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)

lst_com1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_com1)

# 13. Convert (2) to regular for with if-else
# (2) list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

lst_2 = []
for num in range(10):
    if num % 2 == 0:
            lst_2.append(num // 2)
    else: lst_2.append(num * 10)
print(lst_2)


# 14. Convert (3) to dict comprehension.
# (3) d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)

lst_com3 = [num ** 2 for num in range(1, 11) if num % 2 == 1 ]
print(lst_com3)

# 15*. Convert (4) to dict comprehension.
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

# lst_test4 = []
# for num in range(1,11):
#     if num % 2 == 1:
#         lst_test4.append(num ** 2)
#     else:
#         lst_test4.append(num // 0.5)
# print(lst_test4)

lst_com4 = [num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1,11)]
print(lst_com4)

# 16. Convert (5) to regular for with if.
# (5) dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# lst_test5 = {num: num ** 3 for num in range(10) if num ** 3 % 4 == 0}
# print(lst_test5)

dict_5 = {}
for x in range(10):
        if x ** 3 % 4 == 0:
            dict_5[x] = x ** 3
print(dict_5)

# 17*. Convert (6) to regular for with if-else.
# (6) dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

dict_6 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_6[x] = x ** 3
    else:
        dict_6[x] = x
print(dict_6)

# Lambda:
# 18. Convert (7) to lambda function
# #(7) def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

foo_lmb = lambda x, y : 'x' if x < y else 'y'
print(foo_lmb(10,20))

# 19*. Convert (8) to regular function
# (8) foo = lambda x, y, z: z if y < x and x > z else y

def foo (x, y, z):
    if y < x and x > z:
        return 'z'
    else:
        return 'y'

print(foo(4,2,5))


# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_map_lmd = list(map(lambda x: x * 2, lst_to_sort))
print(lst_map_lmd)

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_map = list(map(lambda x, y: x ** y, list_A, list_B))
print(lst_map)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

from functools import reduce

print(reduce(lambda x, y : x*y, lst_to_sort))

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

lst_flt_lmd = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_flt_lmd)

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

lst_flt_lmd2 = list(filter(lambda x: x<0, range(-10, 10)))
print(lst_flt_lmd2)

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)
