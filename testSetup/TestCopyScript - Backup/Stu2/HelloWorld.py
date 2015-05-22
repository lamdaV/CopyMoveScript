"""
Testing Automation for Python.

Created on May 2, 2015.
Written by: lamd.
"""
import math

def main():
    """
    Test your functions here
    """
    print("Function\tExpected\tActual")
    print("Hello World:\t{0}\t{1}".format("Hello World", helloWorld()))
    print("Sum:\t\t{0}\t\t{1}".format(5, sum2(2, 3)))
    print("Distance:\t{0}\t\t{1}".format(5, distance(1, 1, 5, 5)))
    print("Summation:\t{0}\t\t{1}".format(6, summation([1, 2, 3])))
    print("CombineString:\t{0}\t{1}".format("helloworld", combineString("hello", "world")))
    print("DivisibleByTwo:\t{0}\t\t{1}".format(True, divisibleByTwo(444)))
    pass

def helloWorld():
    """ 
    Make the classic HelloWorld program in Python.
    """
    return "Hello World"

def sum2(x, y):
    """ 
    Make a basic summation function between two integers. 
    
    Preconditions:
        :type x : int
        :type y : int
    """

    return x + y

def distance(x1, y1, x2, y2):
    """ 
    Return the distance between the two given numbers.
    
    Hint: Explore the Math (Use Math(dot)) and find useful functions to
    solve.
    
    Preconditions:
        :type x1: int
        :type x2: int
        :type y1: int
        :type y2: int
    """

    dx = math.pow((x1 - x2), 2)
    dy = math.pow((y1 - y2), 2)
    return int(math.sqrt(dx + dy))

def summation(listOfNums):
    """
    Return the total of the values within the given array.
    
    DO NOT USE THE SUM() FUNCTION.
    
    Hint: Use a for loop. If you are daring, use a while loop. If you are an
    expert, use recursion.
    
    Preconditions:
        :type listOfNums: list
    """
    total = 0
    for k in range(0, len(listOfNums)):
        total = total + listOfNums[k]
    return total

def combineString(x, y):
    """
    Combine the two given strings.
    
    Example: If the strings "Hello" and "World" were given, the result would
    be "HelloWorld."
    
    Preconditions:
        :type x: str
        :type y: str
    """
    return x + y

def divisibleByTwo(x):
    """
    Return a Boolean value indicating if the number is divisible by 2.

    Hint: Use the modulus operator (%).
    
    Preconditions:
        :type x: int
    """
    if (x % 2 == 0):
        return True
    return False

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
