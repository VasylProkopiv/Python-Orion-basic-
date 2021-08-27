

person = {'name': 'vasya', 'surname': 'pupkin', 'email': 'test@test.com'}

dict_1 = dict(name='petro', tel='1234')

# завдяки get ми можемо отримати не виключення та повідомлення а None якщо не матимемо такого ключа у дікті
# telefon = person.get('tel')
# print(telefon)

# завдяки get та аргументу "12345678" ми підставляємо аргумент при умові що ключа тел у цьому дікті немає
# telefon = person.get('tel', '12345678')
# print(telefon)
# print(person)

# цей приклад показує, що значення ключа в дікті є сильнішим ніж аггуммент і виведеться 1234
# telefon = dict_1.get('tel', '12345678')
# print(telefon)

# цей приклад показує як добавити ключ тел і значення 12345678 у словник персон
# telefon = person.setdefault('tel', '12345678')
# print(telefon)
# print(person)

# викликаємо список кортежів(фрозен ліст) циклом фор
# for item in person.items():
#     print(item)

# вивести не друк ключ та значення
# for key, value in person.items():
#     print(key, value)

# метод update поновлює дані словника
# new = {'name': 'Christina', 'tel': '000222'}
# person.update(new)
# print(person)

# приклад що таке ноне
# def a():
#     print('Hello world')
#     return None
#
# result = a()
# print(result)
