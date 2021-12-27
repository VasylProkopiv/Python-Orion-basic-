import doctest
from math import sqrt


class Calc:
    @staticmethod
    def sum(a, b):
        """ Sum of two numbers.
        >>> Calc.sum(1, 99)
        100
        >>> Calc.sum(1.0, 1)
        2.0
        >>> Calc.sum(-2, 1)
        -1
        >>> Calc.sum(-2, -1)
        -3

        :param a: first number, int/float
        :param b: second number, int/float
        :return: sum of values, int/float
        """
        return a + b

    @staticmethod
    def diff(a, b):
        """ Diff of two numbers.
        >>> Calc.diff(100, 10)
        90
        >>> Calc.diff(0, 50.0)
        -50.0
        >>> Calc.diff(-10, -50.0)
        40.0

        :param a: first value, int/float
        :param b: second value, int/float
        :return: diff of values, int/float/Exception
        """
        return a - b

    @staticmethod
    def mul(a, b):
        """ Multiplication of two numbers.
        >>> Calc.mul(-1, 1)
        -1
        >>> Calc.mul(1, 10.0)
        10.0

        :param a: first value, int/float
        :param b: second value, int/float
        :return: multiplication of values, int/float
        """

        return a * b

    @staticmethod
    def div(a, b):
        """ Division of two numbers.
        >>> Calc.div(0.0, 1)
        0.0
        >>> Calc.div(-2, 1)
        -2
        >>> Calc.div(2, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

        :param a: first value, int/float
        :param b: second value, int/float
        :return: division of values, float/Exception
        """
        return round((a / b), 2)

    @staticmethod
    def pow(a, b):
        """ Rise a-number to the b-power.
        >>> Calc.pow(0.0, 0)
        1.0
        >>> Calc.pow(0.0, 1)
        0.0
        >>> Calc.pow(-2, 3)
        -8

        :param a: value, int/float
        :param b: power, int/float
        :return: rise any number to the power, int/float/Exception
        """
        return a ** b

    @staticmethod
    def sqrt(a) -> float:
        """ The sqrt of a number.
        >>> Calc.sqrt(4.0)
        2.0
        >>> Calc.sqrt(25)
        5.0
        >>> Calc.sqrt(-25)
        Traceback (most recent call last):
            ...
        ValueError: math domain error

        :param a: value, int/float
        :return: square root of any number, float
        """
        return sqrt(a)

    @staticmethod
    def perc(a, b) -> float:
        """ The percentage a from number b.
        >>> Calc.perc(100, 50)
        50.0
        >>> Calc.perc(-1, 0) # doctest: +SKIP
        0.0
        >>> Calc.perc(10, 100)
        10.0

        :param a: percent, int/float
        :param b: value, int/float
        :return: percentage of any number, float/Exception
        """
        return (a * b) / 100


if __name__ == "__main__":
    doctest.testmod()



