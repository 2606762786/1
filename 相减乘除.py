
class Calc:
    def add(self,a,b):
        return a+b

    def multiply(self,a,b):
        return a-b

    def minus(self,a,b):
        return  a * b

    def Divided(self,a,b):
        return a / b



#乘法
from unittest import TestCase
from demo import Calc
class TestCalc(TestCase):
    def multiply1(self):
        a = 4
        b = 6
        c = 24

        calc = Calc()
        sum = calc.multiply(a, b)

        self.assertEqual(c,sum)

    def multiply2(self):
        a = 5
        b = 2
        c = 10

        calc = Calc()
        sum = calc.multiply2(a, b)

        self.assertEqual(c,sum)

#减法
from unittest import TestCase
from demo import Calc

class testCalc(TestCase):

    def minus1(self):

         a = 4
         b = 6
         c = -2

         calc = Calc()
         sum = calc.minus(a,b)

         self.assertEqual(c,sum)

    def minus2(self):
        a = 6
        b = 4
        c = 2

        calc = Calc()
        sum = calc.minus(a, b)

        self.assertEqual(c, sum)

#除法
from unittest import TestCase
from demo import Calc

class testCalc(TestCase):

    def testDev1(self):

         a = 6
         b = 3
         c = 2

         calc = Calc()
         sum = calc.Divided(a,b)

         self.assertEqual(c,sum)

    def testDv2(self):
        a = 6
        b = 3
        c = -2

        calc = Calc()
        sum = calc.Divided(a, b)

        self.assertEqual(c, sum)






















