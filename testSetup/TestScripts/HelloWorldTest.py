'''
Created on May 2, 2015

@author: lamd
'''
import unittest
import random
import HelloWorld as hw

class Test(unittest.TestCase):

    def testHelloWorld(self):
        self.assertEqual("Hello World", hw.helloWorld(), "helloWorld failed")

    def testSum2(self):
        failedMessage = "Sum Failed"
        self.assertEqual(5, hw.sum2(2, 3), failedMessage)
        self.assertEqual(4, hw.sum2(2, 2), failedMessage)
        self.assertEqual(10, hw.sum2(7, 3), failedMessage)
        self.assertEqual(90, hw.sum2(40, 50), failedMessage)
        self.assertEqual(15, hw.sum2(7, 8), failedMessage)
        self.assertEqual(0, hw.sum2(1, -1), failedMessage)
        self.assertEqual(0, hw.sum2(0, 0), failedMessage)

    def testDistance(self):
        failedMessage = "Distance Failed"
        self.assertEqual(0, hw.distance(0, 0, 0, 0), failedMessage)
        self.assertEqual(6, hw.distance(3, 3, 9, 3), failedMessage)
        self.assertEqual(31, hw.distance(30, 2, -1, 8), failedMessage)
        self.assertEqual(2, hw.distance(1, 1, 2, 3), failedMessage)

    def testSummation(self):
        listOfInts = []
        for _ in range(3):
            listOfInts.append(random.randint(1, 100))

        self.assertEqual(sum(listOfInts), hw.summation(listOfInts), "Summation Failed")

    def testCombineStrint(self):
        failedMessage = "combineString Failed"
        self.assertEqual("HelloWorld", hw.combineString("Hello", "World"), failedMessage)
        self.assertEqual("RainFall", hw.combineString("Rain", "Fall"), failedMessage)
        self.assertEqual(":-)", hw.combineString(":-", ")"), failedMessage)

    def testDivisibleByTwo(self):
        failedMessage = "divisibleByTwo Failed"
        self.assertEqual(True, hw.divisibleByTwo(2), failedMessage)
        self.assertEqual(True, hw.divisibleByTwo(4), failedMessage)
        self.assertEqual(True, hw.divisibleByTwo(108), failedMessage)
        self.assertEqual(True, hw.divisibleByTwo(10008), failedMessage)
        self.assertEqual(False, hw.divisibleByTwo(3), failedMessage)
        self.assertEqual(False, hw.divisibleByTwo(7), failedMessage)
        self.assertEqual(False, hw.divisibleByTwo(901), failedMessage)
        self.assertEqual(False, hw.divisibleByTwo(90000001), failedMessage)

unittest.main()
