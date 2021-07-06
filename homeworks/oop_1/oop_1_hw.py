# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_statistic(self):
        print(f'The vehicle max speed: {self.max_speed} m/h\nThe vehicle mileage: {self.mileage} miles')


Dodge = Vehicle(300, 17000)
Dodge.get_statistic()


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def get_seating_capacity(self):
        print(f'The bus seating capacity: {self.seating_capacity}')


ikarus = Bus(100, 15000, 42)
ikarus.get_seating_capacity()

# 3. Determine which class a given Bus object belongs to (Check type of an object)
electron = Bus(42, 100, 20000)
print('The type of the electron:', type(electron).__name__)
print('The object is Bus:', isinstance(electron, Bus))
print('The object is Vehicle:', isinstance(electron, Vehicle))
print('The Bus is a subclass of the Vehicle:', issubclass(Bus, Vehicle))

# 4. Determine if School_bus is also an instance of the Vehicle class
School_bus = Bus(40, 70, 120000)
print('The object is Vehicle:', isinstance(School_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def statistic(self):
        print(f'The number of students: {self.number_of_students}')


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own -
# bus_school_color
class SchoolBus(Bus, School):
    def __init__(self, bus_school_color, seating_capacity, max_speed, mileage, get_school_id, number_of_students):
        Bus.__init__(self, seating_capacity, max_speed, mileage)
        School.__init__(self, get_school_id, number_of_students)
        self.bus_school_color = bus_school_color

    def color(self):
        print(f'The SchoolBus color is: {self.bus_school_color}')


CitySchoolBus = SchoolBus('yellow', 30, 70, 35000, 'yes', 34)
CitySchoolBus.color()


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.
class Bear:
    def make_sound(self):
        print('Roar')


class Wolf:
    def make_sound(self):
        print('Howl')


grizzly = Bear
polar_wolf = Wolf

for predators in (grizzly, polar_wolf):
    predators.make_sound('')


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population
# > 1500, otherwise return message: "Your city is too small".
class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return 'Your city is too small'

    def __init__(self, name, population):
        self.name = name
        self.population = population


new_city1 = City('city1', 500)
print(new_city1)
new_city2 = City('city2', 25000)
print(new_city2)


# 9. Override a printable string representation of the City class and return: The population of the city {name} is {
# population}
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"


new_city3 = City('city3', 30000)
print(new_city3)


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater
# than 10. And perform this add (+) of two instances.
class NewAdd:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        if y.x > 10 or self.x > 10:
            return self.x * y.x
        else:
            return self.x + y.x


x1 = NewAdd(1)
x2 = NewAdd(7)
print(x1 + x2)

x1 = NewAdd(10)
x2 = NewAdd(7)
print(x1 + x2)


# 11. The __call__ method enables Python programmers to write
# classes where the instances behave like functions and can be called like a function. Create a new class with
# __call__ method and define this call to return sum.
class ReturnSum:
    def __call__(self, *args):
        summa = 0
        summa = sum(args)
        return summa


ex = ReturnSum()
print(ex(5, 6, 7, 10))


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes. Override the __bool__magic method considered to be
# truthy if the length of the cart list is non-zero. e.g.: order_1 = MyOrder(['a', 'b', 'c'], 'd') order_2 = MyOrder(
# [], 'a') bool(order_1) True bool(order_2) False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) != 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))
