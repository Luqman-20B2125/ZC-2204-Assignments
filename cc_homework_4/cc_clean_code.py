import math
from abc import ABC, abstractmethod
# Implementation hidden behind abstraction
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Square(ABC): # we abstract square so that user does not know if square has length saved or the points saved
 
    @abstractmethod
    def __init__(self):
        pass

    def getLength(self):              
        return self.length

    def getArea(self):
        return self.length * self.length
    
    def getPerimeter(self):
        return self.length * 4
 
class Square1(Square):
 
    def __init__(self, length):
        self.length = length
 
class Square2(Square):
 
    def __init__(self, point1Horizontal, point2Horizontal): 
                                        # Only two points needed as to get length we only need two points
                                        # and since this is a square we don't need the other two points
        self.point1 = point1Horizontal
        self.point2 = point2Horizontal
        xSquare = math.pow((self.point1.getX() - self.point2.getX()),2)
        ySquare = math.pow((self.point1.getY() - self.point2.getY()),2)
        self.length = math.sqrt(xSquare + ySquare)

s1 = Square1(3)
s2 = Square2(Point(0, 0), Point(3, 0))
print(s1.getLength())
print(s2.getLength())
print(s1.getArea())
print(s2.getArea())
print(s1.getPerimeter())
print(s2.getPerimeter())

# Law of Demeter Violation Fixed
def returnObjectLength(object):
    return object.getLength() # no longer violates law of demeter as the method being called is from an object passed into the function

print(returnObjectLength(s2)) # no longer a trainwreck as what was previously done in code is now covered by calling one function

# Using exception handling for errors instead
def sumNumber(value1, value2):
    try:
        a = int(value1)
        b = int(value2)
        print("Sum of value1 and value2 is ", (a + b))
    except:
        print ("value1 or value2 is not a number, so it cannot be summed, as attempting to typecast one of them to int caused an error.")
        # exception thrown now informs of cause of error and where the error occured

sumNumber('a',2)
sumNumber(1,'a')
sumNumber(1, 2)
