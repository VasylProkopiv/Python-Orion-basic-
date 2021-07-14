from abc import abstractmethod


# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, seating_capacity, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


# 3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(Bus))
# <class 'type'>


# 4. Determine if School_bus is also an instance of the Vehicle class
School_bus = Bus('40', '130', '1000000')
print(type(School_bus))


# <class '__main__.Bus'>

# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, bus_school_color, school_id, number_of_students, seating_capacity, max_speed, mileage):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, seating_capacity, max_speed, mileage)
        self.bus_school_color = bus_school_color


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,make a tuple of it and by using for call their action using the same method.


class Bear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self, sound=''):
        print(sound)
        print('gr-gr-gr')


class Wolf:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def make_sound(self, sound=''):
        print(sound)
        print('puff-puff')


akela = Wolf('Akela', 50)
ballu = Bear('Ballu', 100)

for animal in (Bear, Wolf):
    animal.make_sound('')


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".


# class City(object):
#     def __new__(cls, name, population):
#         if population > 1500:
#             return object
#         else:
#             print('Your city is too small')
#
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#
# madrid = City('Madrid', 3000000)
# kovjary = City('Kovjary', 1200)
# print('return > 1500', madrid)
# print('return < 1500', kovjary)
#
#
# class City():
#     def __new__(cls, name, population):
#         super().__new__(cls)
#         if population > 1500:
#             return cls
#         else:
#             print('Your city is too small')
#
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#
# madrid = City('Madrid', 3000000)
# kovjary = City('Kovjary', 1200)
# print('return > 1500', madrid)
# print('return < 1500', kovjary)


# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}


class City():
    def __new__(cls, name, population):
        super().__new__(cls)
        if population > 1500:
            return cls

        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        if population > 1500:
            print(f'The population ot the city {self.name} is {self.population}')


madrid = City('Madrid', 3000000)
kovjary = City('Kovjary', 1200)

# class City(object):
#     def __new__(cls, name, population):
#         if population > 1500:
#             return object
#             # print(f'The population ot the city {self.name} is {self.population}')
#         else:
#             print('Your city is too small')
#
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#         print(f'The population ot the city {self.name} is {self.population}')
#
# madrid = City('Madrid', 3000000)
# kovjary = City('Kovjary', 1200)
