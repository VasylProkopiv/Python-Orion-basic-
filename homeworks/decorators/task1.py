import time

# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції


def decor_time(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(f'Function worked {time.time() - t1} seconds')
        return result
    return wrap


@decor_time
def user_input():
    new_list = []
    text = input('Please write your text or "enter + Q + enter" to exit:')
    while text != 'Q':
        new_list.append(text)
        text = input()
    return new_list


decor_time(user_input())



