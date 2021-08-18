# 1. Написати програму яка буде обраховувати два квадратних рівняня одночасно, всі параметри рівняння задати в змінні.

import logging
import threading
import time
import math


def thread_function(name, a, b, c):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info(f"Thread {name}: {a} * x^2 + {b} * x + {c} = 0")
    d = b**2 - 4*a*c
    if d < 0:
        logging.info("This equation has no real solution")
    elif d == 0:
        x = -b / (2*a)
        logging.info(f"Thread {name}: x1 = {x}")
    else:
        x1 = (-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        x2 = (-b - math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        logging.info(f"Thread {name}: x1 = {x1}, x2 = {x2}")
    logging.info("Thread %s: finishing", name)


format_ = "%(asctime)s: %(message)s"
logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")
x1 = threading.Thread(target=thread_function, args=('1st', 1, -2, -3))
x2 = threading.Thread(target=thread_function, args=('2nd', 1, 5, -6))
x1.start()
x2.start()


