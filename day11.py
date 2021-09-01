class Calc:
    def add(self,a,b):
        return a + b

    def subs(self,a,b):
        return a - b

    def multi(self,a,b):
        return  a * b

    def devision(self,a,b):
        return a // b


from calc import Calc
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack

dd = [
    [2,2,4],
    [6,9,54],
    [-9,-9,81],
    [-9,8,-72],
    [14,10,140],
    [5,6,30]
]

@ddt
class TestCalcmulti(TestCase):

    @data(*dd)
    @unpack
    def testmulti(self,a,b,c):
        calc  = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(sum,c)

from calc import Calc
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack


dd = [
    [4,-2,-2],
    [6,3,2],
    [9,3,3],
    [24,8,3],
    [66,11,6],
    [15,3,5]
]

@ddt
class TestCalcdevision(TestCase):

    @data(*dd)
    @unpack
    def testdevision(self,a,b,c):
        calc  = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(sum,c)


import  unittest
from HTMLTestRunner import HTMLTestRunner
import os
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算器测试报告",
    description="这是计算器加法和减法测试报告",
    verbosity=1,
    stream = open(file="计算器测试报告.html",mode="w+",encoding="utf-8")
)

#
runner.run(tests)
