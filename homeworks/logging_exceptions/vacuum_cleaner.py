import time
from random import randint


class LowBattery(Exception):
    pass


class DischargedBattery(Exception):
    pass


class LowWater(Exception):
    pass


class EmptyWater(Exception):
    pass


class FullBag(Exception):
    pass


class AlmostFullBag(Exception):
    pass


class Stop(Exception):
    pass

# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек - DONE
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner" - DONE
# (в цих функціях повинні стояти прінти "wash" і "vacuum cleaner" відповідно), - DONE
#також на кожній ітерації прінтиться "move" - DONE
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі), - DONE
# а кількість сміття збільшується на рандомне ціле число в межах від 0 до 10 - DONE
#
# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0,
# кількість сміття більша ніж певне число.
# Опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
#
# можете придумати ще свої ексепшини і як їх опрацьовувати


class RobotVacuumCleaner:

    def __init__(self, battery_charge, water_level, bag):
        self.battery_charge = int(battery_charge)
        self.bag = bag
        self.water_level = water_level
        self.water_consumption = 10
        self.buttery_consumption = 10

    def wash(self):
        if self.water_level > 0:
            self.water_level -= self.water_consumption
            print('Wash')

        if self.water_level <= 0:
            raise EmptyWater

        if self.water_level < 20:
            raise LowWater

    def vacuum_cleaning(self):
        if self.bag < 100:
            self.bag += randint(0, 10)
            print('Clean')

        if self.bag >= 100:
            raise FullBag

        if 100 > self.bag > 80:
            raise AlmostFullBag

    def move(self):
        self.battery_charge -= self.buttery_consumption
        print("Move")

        if self.battery_charge <= 0:
            raise DischargedBattery
        if self.battery_charge <= 20:
            raise LowBattery

        if self.water_level > 0:
            self.wash()
        if self.bag < 100:
            self.vacuum_cleaning()
        time.sleep(1)


robot = RobotVacuumCleaner(50, 50, 80)

while True:
    try:
        print('_____________________________________________________________________________________________________')
        print(f'Battery charge = {robot.battery_charge}, Water level = {robot.water_level}, Bag is {robot.bag}% full')
        robot.move()

    except LowBattery:
        print('I need to be charged! Only 20% till the dead end!')
        if robot.water_level > 0:
            try:
                robot.wash()
            except LowWater:
                print('The water is running out! Only 20% till the dead end!')
            except EmptyWater:
                print('No water! Now I can only clean ')

        elif robot.bag < 100:
            try:
                robot.vacuum_cleaning()
            except AlmostFullBag:
                print('I am almost full!')
            except FullBag:
                print('I am full! No longer efficient :( ')
        time.sleep(1)

    except DischargedBattery:
        print('That is the end! Put me to the charger!')
        break

    except LowWater:
        print('Need water! Only 20% till the dead end!')
        if robot.bag < 100:
            try:
                robot.vacuum_cleaning()
            except AlmostFullBag:
                print('I am almost full!')
            except FullBag:
                print('I am full! No longer efficient :( ')
        time.sleep(1)

    except EmptyWater:
        print('No water! Now I can only clean!')
        if robot.bag < 100:
            try:
                robot.vacuum_cleaning()
            except AlmostFullBag:
                print('I am almost full!')
            except FullBag:
                print('I am full! No longer efficient :( ')
        time.sleep(1)

    except AlmostFullBag:
        print('I am almost full!')
        if robot.water_level > 0:
            try:
                robot.wash()
            except LowWater:
                print('Need water! Only 20% till the dead end!')
            except EmptyWater:
                print('No water! Now I can only clean!')
        time.sleep(1)

    except FullBag:
        print('I am full! No longer efficient :( ')
        if robot.water_level > 0:
            try:
                robot.wash()
            except LowWater:
                print('Need water! Only 20% till the dead end!')
            except EmptyWater:
                print('No water! Now I can only clean!')
        time.sleep(1)

    finally:
        print('Uhhh...I need a rest!')