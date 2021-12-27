import random
import time
from threading import Thread
import logging
from math import sqrt


class EquationError(Exception):
    pass


class MyThread(Thread):
    def __init__(self, name, a, b, c):
        Thread.__init__(self)
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def quadratic_equation(self):
        logging.info(f"Thread {self.name}: {self.a} * x^2 + {self.b} * x + {self.c} = 0")
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            logging.info(f"This equation has no real solution")
            return None
        elif d == 0:
            x = -self.b / (2 * self.a)
            logging.info(f"Thread {self.name}: x = {x}")
            return x
        else:
            x1 = (-self.b + sqrt((self.b ** 2) - (4 * (self.a * self.c)))) / (2 * self.a)
            x2 = (-self.b - sqrt((self.b ** 2) - (4 * (self.a * self.c)))) / (2 * self.a)
            logging.info(f"Thread {self.name}: x1 = {x1}, x2 = {x2}")
            return x1, x2

    def run(self):
        amount = random.randint(1, 4)
        time.sleep(amount)
        logging.info("%s is running" % self.name)
        try:
            if self.a != 0:
                self.quadratic_equation()
            else:
                raise EquationError
        except EquationError:
            logging.error("Error. The first coefficient can not be equal to 0")

        logging.info("Thread %s: finishing" % self.name)


format_ = "%(asctime)s: %(message)s"
logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")

thread_1 = MyThread("Thread 1", a=1, b=-2, c=-3)
thread_2 = MyThread("Thread 2", a=1, b=5, c=-6)
logging.info("Threads starting")
thread_1.start()
thread_2.start()

