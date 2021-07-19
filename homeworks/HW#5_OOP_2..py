import dataclasses
from collections import namedtuple


# 1.
# class Laptop:
#     Make the class with composition.
# class Battery:
#     Make the class with composition.

class Laptop:
    def __init__(self):
        battery = Battery


class Battery:
    def __init__(self):
        pass


# 2.
# class Guitar:
#     Make the class with aggregation
# class GuitarString:
#     Make the class with aggregation

class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self):
        pass


guitar_string_1 = GuitarString
guitar_1 = Guitar(guitar_string_1)


# 3.
# class Calc:
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static

class Calc:

    @staticmethod
    def add_nums(x, y, z):
        return x + y + z


print(Calc.add_nums(2, 3, 4))


# 4*.
# class Pasta:
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
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
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

    def __repr__(self):
        return f'with {self.ingredients}'


pasta_1 = Pasta(['tomato', 'cucumber'])
print('pasta_1', pasta_1)
pasta_2 = Pasta.bolognaise()
print('pasta_2', pasta_2)


# 5*.
# class Concert:
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50

class Concert:
    def __init__(self, max_visitors_num):
        self.max_visitors_num = max_visitors_num

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, count):
        self._visitors_count = count if count < self.max_visitors_num else f'# {self.max_visitors_num}'


concert_1 = Concert(50)
concert_1.visitors_count = 1000
print(concert_1.visitors_count)


# 6.
# class AddressBookDataClass:
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7. Create the same class (6) but using NamedTuple

AddressBookDataClass = namedtuple('AddressBookDataClass',
                                  ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


# 8.
# class AddressBook:
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.

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
        return f'key = {self.key}, name = {self.name}, phone_number = {self.phone_number}, address = {self.address}, email = {self.email}, birthday = {self.birthday}, age = {self.age}'


my_address_book = AddressBook('1', 'Vasyl', '0966035000', 'Lviv', 'media@gmail.com', '13.03.1985', 36)
print(my_address_book)


# 9.
# class Person:
#     Change the value of the age property of the person object
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    name = 'John'
    age = 36
    country = 'USA'


john = Person
setattr(john, 'age', 26)
print(john.age)


# 10.
# class Student:
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def student_email(self):
        return self._student_email

    @student_email.setter
    def student_email(self, email):
        self._student_email = email


student = Student(13, 'Vasyl')
student.student_email = 'www@fff.ua'
print(student.student_email)

# 11*.
# class Celsius:
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
