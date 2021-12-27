
# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних


def decor_str(func):
    def wrap(n):
        result = func(n)
        new_list = [str(i) for i in result]
        return new_list
    return wrap


@decor_str
def create_list(n):
    return list(range(n+1))


print(create_list(6))

