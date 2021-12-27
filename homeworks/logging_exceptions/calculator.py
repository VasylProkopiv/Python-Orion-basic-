import logging
import math


class Calculator:
    def __init__(self, x, op, y):
        self.x = x
        self.y = y
        self.op = op

    def add(self):
        res_sum = self.x + self.y
        return print(f'{self.x} + {self.y} = {res_sum}')

    def subtract(self):
        res_dif = self.x - self.y
        return print(f'{self.x} - {self.y} = {res_dif}')

    def multiply(self):
        res_mlt = self.x * self.y
        return print(f'{self.x} * {self.y} = {res_mlt}')

    def divide(self):
        res_div = self.x / self.y
        return print(f'{self.x} / {self.y} = {res_div}')

    def exponentiation(self):
        res_exp = self.x ** self.y
        return print(f'{self.x} ^ {self.y} = {res_exp}')

    def sqrt(self):
        res_sqrt = math.sqrt(self.x)
        return print(f'The sqrt of {self.x} = {res_sqrt}')

    def percentage(self):
        res_prc = (self.x * self.y)/100
        return print(f'The {self.y}% of {self.x} is {res_prc}')


log_template = "%(levelname)s: %(filename)s: %(message)s"
logging.basicConfig(level=logging.INFO, filename="Calculator.log", filemode="a", format=log_template)


while True:
    input1 = input('Enter a first number, or type STOP to turn off the calculator ')
    if input1 == 'STOP':
        break
    operation = input('Enter an operation (+, -, *, /, **, sqrt or %) ')
    if operation == 'sqrt':
        input2 = input('Enter 1 ')
    else:
        input2 = input('Enter a second number ')

    calc = Calculator(input1, operation, input2)
    print('\n________________________________________________________________\n')

    try:
        calc.x = float(calc.x)
        calc.y = float(calc.y)
        try:
            if operation == '+':
                calc.add()
                logging.info("The '+' operation has been called")
            elif operation == '-':
                calc.subtract()
                logging.info("The '-' operation has been called")
            elif operation == '*':
                calc.multiply()
                logging.info("The '*' operation has been called")
            elif operation == '/':
                calc.divide()
                logging.info("The '/' operation has been called")
            elif operation == '**':
                calc.exponentiation()
                logging.info("The '**' operation has been called")
            elif operation == 'sqrt':
                calc.sqrt()
                logging.info("The 'sqrt' operation has been called")
            elif operation == '%':
                calc.percentage()
                logging.info("The '% of number' operation has been called")

        except ZeroDivisionError:
            if operation == "/":
                print("Division by 0")
                logging.error("Division by 0")

    except ValueError:
        print('That is not valid number')
        logging.error("Entered number must be a float type")




