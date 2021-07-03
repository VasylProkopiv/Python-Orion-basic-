# 1. Define the id of next variables:
int_a = 55
print('#1: ', id(int_a))
str_b = 'cursor'
print('#1: ', id(str_b))
set_c = {1, 2, 3}
print('#1: ', id(set_c))
lst_d = [1, 2, 3]
print('#1: ', id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('#1: ', id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
print('#2: ', id(lst_d))
lst_d.append(5)
print('#2: ', id(lst_d))

# 3. Define the type of each object from step 1.
print('#3: ', type(int_a))
print('#3: ', type(str_b))
print('#3: ', type(set_c))
print('#3: ', type(lst_d))
print('#3: ', type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print('#4: ', isinstance(int_a, int))
print('#4: ', isinstance(str_b, str))
print('#4: ', isinstance(set_c, set))
print('#4: ', isinstance(lst_d, list))
print('#4: ', isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
a = 5
b = 3
print('#5: ', 'Anna has {} apples and {} peaches'.format(a, b))

# 6. By passing index numbers into the curly braces.
print('#6: ', 'Anna has {1} apples and {0} peaches'.format(7, 4))

# 7. By using keyword arguments into the curly braces.
print('#7: ', 'Anna has {apple} apples and {peach} peaches'.format(apple=2, peach=3))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('#8: ', 'Anna has {0:5} apples and {1:3} peaches'.format(2, 3))

# 9. With f-strings and variables
apple = 'two'
peach = 'nine'
print('#9: ', f'Anna has {apple} apples and {peach} peaches')

# 10. With % operator
apple = 8
peach = 10
print('#10: ', 'Anna has %d apples and %d peaches' % (apple, peach))

# 11*. With variable substitutions by name (hint: by using dict)
key_dictionary = {"apple": "two", "peach": "ten"}
print('#11: ', 'Anna has {apple} apples and {peach} peaches'.format(**key_dictionary))

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

# 12. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print('#12: ', list_comprehension)

# (2)
lst_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(lst_comprehension)

# 13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print('#13: ', lst)

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# 14. Convert (3) to dict comprehension.
d_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print('#14: ', d_comp)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# 15*. Convert (4) to dict comprehension.
d_comp_2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print('#15: ', d_comp_2)

# (5)
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(dict_comprehension)

# 16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print('#16: ', d)

# (6)
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

# 17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print('#17: ', d)


# Lambda:

# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y


# 18. Convert (7) to lambda function
foo_lmd = lambda x, y: x if x < y else y

print('#18: ', foo_lmd(4, 7))
print('#18: ', foo_lmd(13, 8))

# (8)
foo = lambda x, y, z: z if y < x and x > z else y

# 19*. Convert (8) to regular function
def foo_n(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print('#19: ', foo_n(4, 2, 5))
print('#19: ', foo_n(6, 2, 5))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print('#20: ', sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to
print('#21: ', sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print('#22: input: ',lst_to_sort)
print('#22: result: ', new_lst_to_sort)

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

map_raise = list(map(lambda x, y: x ** y, list_A, list_B))
print('#23: ', map_raise)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce

comp = reduce((lambda x, y: x + y), lst_to_sort)
print('#24: ', comp)

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
flt_lst = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print('#25: input: ', lst_to_sort)
print('#25: result: ', flt_lst)

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
flt_lst1 = list(filter(lambda x: (x < 0), range(-10, 10)))
print('#26: ', flt_lst1)

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

flt_lst = list(filter(lambda x: (x in list_2), list_1))
print('#27: ', flt_lst)