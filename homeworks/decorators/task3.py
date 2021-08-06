
# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних


def decor_convert(func):
    def wrap(ls):
        new_list = []
        for i in ls:
            try:
                i = float(i)
                new_list.append(i)
            except ValueError:
                continue
        return func(new_list)
    return wrap


@decor_convert
def add_list(list_ex):
    return sum(list_ex)


list1 = [1, 2, '3', 4, '5', "CURSOR", '6.0', '7.1', 7.9, 9, 'END']
print(f'The sum of all elements is {add_list(list1)}')


