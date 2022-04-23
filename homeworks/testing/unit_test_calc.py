from unittest import TestCase
from calc import Calc


class TestSum(TestCase):
    """
    Testing summ of numbers in Calc
    """

    def test_001(self):
        print('Test data types sum')
        self.assertIsInstance(Calc.sum(1, 1), int)
        self.assertIsInstance(Calc.sum(1.0, 1.0), float)
        self.assertIsInstance(Calc.sum(1, 1.0), float)

    def test_002(self):
        print('Positive sum test cases')
        self.assertEqual(Calc.sum(0.0, 0), 0)
        self.assertEqual(Calc.sum(1, 1), 2.0)
        self.assertEqual(Calc.sum(-1, 1), 0)
        self.assertEqual(Calc.sum(-10, 5.0), -5)
        self.assertNotEqual(Calc.sum(-10, 5), 5)

    def test_003(self):
        print('Test raise exceptions for sum')
        with self.assertRaises(TypeError):
            Calc.sum("1", 1)


class TestDiff(TestCase):
    """
    Testing diff of numbers in Calc
    """

    def test_101(self):
        print('Test data types diff')
        self.assertIsInstance(Calc.diff(1, 1), int)
        self.assertIsInstance(Calc.diff(1.0, 1.0), float)
        self.assertIsInstance(Calc.diff(1, 1.0), float)

    def test_102(self):
        print('Positive diff test cases')
        self.assertEqual(Calc.diff(0.0, 0), 0)
        self.assertEqual(Calc.diff(-1, -1), 0.0)
        self.assertEqual(Calc.diff(-2, 1), -3)
        self.assertEqual(Calc.diff(-10, -6.0), -4)
        self.assertNotEqual(Calc.diff(2, 1.0), -1)

    def test_103(self):
        print('Test raise exceptions for diff')
        with self.assertRaises(TypeError):
            Calc.diff(1, "1")


class TestMul(TestCase):
    """
    Testing multiplication of numbers in Calc
    """

    def test_201(self):
        print('Test data types mul')
        self.assertIsInstance(Calc.mul(1, 1), int)
        self.assertIsInstance(Calc.mul(1.0, 1), float)

    def test_202(self):
        print('Positive mul test cases')
        self.assertEqual(Calc.mul(0.0, 1), 0)
        self.assertEqual(Calc.mul(1, 2.0), 2.0)
        self.assertEqual(Calc.mul(-1.0, 2), -2.0)
        self.assertEqual(Calc.mul(-1, -1), 1.0)
        self.assertNotEqual(Calc.mul(-1, -1), -1.0)

    def test_203(self):
        print('Test raise exceptions for mul')
        with self.assertRaises(TypeError):
            Calc.mul("1", "1")


class TestDiv(TestCase):
    """
    Testing division of numbers in Calc
    """

    def test_301(self):
        print('Test data types div')
        self.assertIsInstance(Calc.div(1, 1), float)
        self.assertIsInstance(Calc.div(1.0, 1), float)
        self.assertIsInstance(Calc.div(10, 3.0), float)

    def test_302(self):
        print('Positive div test cases')
        self.assertEqual(Calc.div(0.0, 1), 0)
        self.assertEqual(Calc.div(10, 2.0), 5.0)
        self.assertEqual(Calc.div(-10.0, 2), -5.0)
        self.assertEqual(Calc.div(-1, -1), 1.0)
        self.assertNotEqual(Calc.div(-1, -1), -1.0)

    def test_303(self):
        print('Test raise exceptions for div')
        with self.assertRaises(ZeroDivisionError):
            Calc.div(1, 0)
        with self.assertRaises(TypeError):
            Calc.div(1, "1")


class TestPow(TestCase):
    """
    Testing rise any number to the power in Calc
    """

    def test_401(self):
        print('Test data types pow')
        self.assertIsInstance(Calc.pow(1, 1), int)
        self.assertIsInstance(Calc.pow(1.0, 1), float)
        self.assertIsInstance(Calc.pow(10, 1.0), float)

    def test_402(self):
        print('Positive pow test cases')
        self.assertEqual(Calc.pow(0.0, 0), 1)
        self.assertEqual(Calc.pow(0, 1), 0.0)
        self.assertEqual(Calc.pow(-1, 3), -1)
        self.assertEqual(Calc.pow(-1, 2), 1)

    def test_403(self):
        print('Test raise exceptions for pow')
        with self.assertRaises(TypeError):
            Calc.pow("1", 2)


class TestRoot(TestCase):
    """
    Testing sqt in Calc
    """
    def test_501(self):
        print('Test data types sqrt')
        self.assertIsInstance(Calc.sqrt(4), float)
        self.assertIsInstance(Calc.sqrt(4.0), float)

    def test_502(self):
        print('Positive sqrt test cases')
        self.assertEqual(Calc.sqrt(0.0), 0)
        self.assertEqual(Calc.sqrt(9), 3)
        self.assertEqual(Calc.sqrt(4.0), 2.0)

    def test_503(self):
        print('Test raise exceptions for sqrt')
        with self.assertRaises(ValueError):
            Calc.sqrt(-4)
        with self.assertRaises(TypeError):
            Calc.sqrt("1")


class TestPerc(TestCase):
    """
    Testing percentage of any number in Calc
    """
    def test_601(self):
        print('Test data types perc')
        self.assertIsInstance(Calc.perc(1, 10), float)
        self.assertIsInstance(Calc.perc(1.0, 10), float)
        self.assertIsInstance(Calc.perc(1, 10.0), float)

    def test_Percentage_Computing(self):
        print('Positive perc test cases')
        self.assertEqual(Calc.perc(0.0, 0), 0)
        self.assertEqual(Calc.perc(10, 100), 10.0)
        self.assertEqual(Calc.perc(-10, 100.0), -10)

    def test_Percentage_SpecialCase(self):
        print('Test raise exceptions for perc')
        with self.assertRaises(TypeError):
            Calc.perc("10", 100)

