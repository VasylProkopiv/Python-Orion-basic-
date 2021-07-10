import dataclasses
from collections import namedtuple

print('task_1')
# 1. Make the class with composition.
class Laptop:
    def __init__(self):
        part1 = Battery(100)
        part2 = Battery(200)
        self.parts = [part1, part2]


class Battery:
    def __init__(self, power):
        self.power = power

    def get_info(self):
        return f'The battery power is {self.power}'


laptop = Laptop()
print(laptop.parts[0].get_info())
print(laptop.parts[1].get_info())


# 2. Make the class with aggregation

class Guitar:
    def __init__(self, s):
        self.s = s


class GuitarString:
    def __init__(self, num):
        self.num = num


s2 = GuitarString(6)
guitar = Guitar(s2)


print('\ntask_3')
# 3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
# Note: this method should be static
class Calc:
    def __init__(self):
        pass

    @staticmethod
    def add_nums(*args):
        return sum(args)


print(Calc.add_nums(6, 7, 100))

print('\ntask_4')
# 4*. Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carabonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(['cheese', 'proshutto'])
print(pasta_1.ingredients)

pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)

pasta_3 = Pasta.carabonara()
print(pasta_3.ingredients)

print('\ntask_5')
# 5*. Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50

# #1 The max_visitors_num limitation by getter

class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = value


Concert.max_visitors_num = 30
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)
concert.visitors_count = 20
print(concert.visitors_count)


# #2 The max_visitors_num limitation by setter


class Concert2:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        if self._visitors_count > self.max_visitors_num:
            return self.max_visitors_num
        else:
            return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = value


Concert2.max_visitors_num = 500
concert2 = Concert2()
concert2.visitors_count = 1000
print(concert2.visitors_count)
concert2.visitors_count = 20
print(concert2.visitors_count)

print('\ntask_6')
# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str),
# email (str), birthday (str), age (int)

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


book1 = AddressBookDataClass(13, 'Boo', '+477777777', 'Address1', 'boo@gmail.com', '01.01.2000', 21)
print(book1)
print(book1.birthday)

print('\ntask_7')
# 7. Create the same class (6) but using NamedTuple
AddressBookDataClass = namedtuple('AddressBookDataClass',
                                  ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

book2 = AddressBookDataClass(13, 'Boo', '+477777777', 'Address1', 'boo@gmail.com', '01.01.2000', 21)
print(book2)
print(book2[1])
print(book2.email)

print('\ntask_8')
# 8. Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#    Make its str() representation the same as for AddressBookDataClass defined above.

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"AddressBook(key={self.key}, name='{self.name}', phone_number='{self.phone_number}', " \
               f"address='{self.address}', email='{self.email}', birthday='{self.birthday}', age={self.age}) "


book = AddressBook(13, 'Max', '+177777777', 'LA', 'max@gmail.com', '01.01.2007', 14)
print(book)


print('\ntask_9')
# 9. Change the value of the age property of the person object


class Person:
    name = "John"
    age = 36
    country = "USA"


person1 = Person()
setattr(person1, 'age', 38)
new_age = getattr(person1, 'age')
print(f' name = "John"\n age = {new_age}\n country = "USA"')

print('\ntask_10')
# 10. Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(13, 'Olya')
setattr(student, 'email', f'{student.name}@gmail.com')
print(f"My name is {student.name} and my e-mail is", getattr(student, 'email'))

print('\ntask_11')
# 11*. By using @property convert the celsius to fahrenheit
#      Hint: (temperature * 1.8) + 32)
class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        value = (self._temperature * 1.8) + 32
        return f'The {self._temperature} by Celsius is equal to {value} by Fahrenheit'


# create an object

temp = Celsius(33)
print(temp.fahrenheit)
