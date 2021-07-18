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


class City(object):
    def __new__(cls, name, population):
        if population > 1500:
            return object
        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population


madrid = City('Madrid', 3000000)
kovjary = City('Kovjary', 1200)
print('return > 1500', madrid)
print('return < 1500', kovjary)


class City():
    def __new__(cls, name, population):

        if population > 1500:
            return super().__new__(cls)
        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population


madrid = City('Madrid', 3000000)
kovjary = City('Kovjary', 1200)
print('return > 1500', madrid)
print('return < 1500', kovjary)


# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}


class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'The population ot the city {self.name} is {self.population}'


madrid = City('Madrid', 3000000)
kovjary = City('Kovjary', 1200)
print(madrid)


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)

        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'The population at the city {self.name} is {self.population}'

    def __add__(self, other):
        if self.population > 10 or other.population > 10:
            return self.population * other.population
        else:
            return self.population + other.population


madrid = City('Madrid', 3000000)
lviv = City('Lviv', 1500000)
kovjary = City('Kovjary', 12000)
print(madrid + lviv)


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Salary:
    total_hour_of_work = 0
    total_salary = 0

    def __init__(self, price_per_hour):
        self.price_per_hour = price_per_hour

    def __call__(self, time_of_work):
        self.total_hour_of_work += time_of_work
        self.total_salary += time_of_work * self.price_per_hour
        return time_of_work * self.price_per_hour


manager = Salary(10)
print('month1', manager(5))
print('month2', manager(6))
print('month3', manager(7))


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 1:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')

print(bool(order_1))
print(bool(order_2))
