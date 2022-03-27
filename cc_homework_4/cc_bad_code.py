# Exposed implementation
class Square:
    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def getArea(self):
        return self.length * self.length
    
    def getPerimeter(self):
        return self.length * 4

square = Square(10)
print(square.getLength())
print(square.getArea())
print(square.getPerimeter())

# Law of Demeter Violation
def returnObject(object):
    return object


print(returnObject(square).getLength()) # violates law of demeter as it calls a method from the object that is returned
                                        # is also a trainwreck

# returning an error code after an error flag is true for errors
def sumNumber(value1, value2):
    if (str(value1).isnumeric()) and (str(value2).isnumeric()): # typecast value1 and value2 so that we can use isnumeric to test
                                                                # if they are numeric values
        print("Sum of value1 and value2 is ", (value1 + value2))
    else:
        print("Fail to sum.") # exception thrown is not descriptive of cause and where it occured

sumNumber('a',2)
sumNumber(1,'a')
sumNumber(1, 2)