from abc import abstractmethod

# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_max_speed(self):
        return self.max_speed

    def get_mileage(self):
        return self.mileage
# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, seating_capacity, max_speed, mileage):
        super(Bus, self).__init__(max_speed,mileage)
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
    def __init__(self, get_school_id, number_of_students):