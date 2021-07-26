from helllo import *
slovnik = {'name': 'Vasyl', 'age': 36, 'course': ['Oop', 'Python']}
slovnik['name'] = 'Christina'
# slovnik['phone'] = '0966035000'
slovnik.update({'name': 'Anna-Maria', 'age': 15, 'course': 'do nothing'})
# print(slovnik.get('phone', 'not found'))
# test_x = slovnik.pop('name')
del slovnik['name']
# print(slovnik.get("name"))
print(len(slovnik))
print(slovnik.items())
# print(test_x)
for key, values in slovnik.items():
    print(key, values)
print(a)
print(f'Hello {__name__}')