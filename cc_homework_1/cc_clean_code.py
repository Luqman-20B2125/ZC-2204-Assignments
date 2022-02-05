name = "Luqman"  # Name is now informative as we now know that the variable contains a name
                 # and no need to mentally map what the variable is supposed to be.

flagBool = True  # Name is now true, as variable now contains a boolean value

zero, one = 0, 0 # Not using L or O, instead use a different variable that does not look similar
if zero == 0: 
    print("1 is", one)

schoolType = "Primary"       # Now names have different meaning and indicates the content 
schoolName = "Stella School" # and no longer redundant as schoolType and schoolName can only be strings.

firstName, fullName = "John", "John Smith"  # Now distinguishes the two variables and their contents

firstMiddleLastName = "John Devan Smith" # Name is now pronounceable and tells us what it contains

dateOfExam = "22/3/2022" # Name is now searchable by entering date or exam

moneyAmount = 1000 # No need to encode the variable as moneyAmount can only be a number

class Application: # Change class name to a noun 
    def __init__(self, data = None):
        self.data = data

def printBook(): # Add or use a verb instead to indicate what the function does
    print("Book")

def printHello(): # Don't use cultural reference, instead directly mention what function does
    print("Hello World!")

def SumTwoIntegers(int1, int2): # Use same word for the same effect on different functions or classes
    sum = int1 + int2           # Remove the prefix as no need to indicate variable is a member, as that info is not needed
    return sum

def SumTwoFloats(float1, float2):
    sum = float1 + float2
    return sum

itemList = ["Banana","Apple","Coconut"] # Use programming technical terms if applicable instead of problem domain terms.

homeCity, homeCountry = "Bandar Seri Begawan", "Brunei Darussalam" # Add context to the variable name to give it meaning

def checkBool(flag): # Make the other jobs of the function be a smaller function to be called, 
                     # so that the main function does not have multiple jobs.
                     # This should also be done for functions with boolean argument.
    if flag == True:
        flagTrue()
    else:
        flagFalse()
    
def flagTrue():
    print("Flag is True")

def flagFalse():
    print("Flag is False")
checkBool(True)

def printRepeatStringNumberOfRepetition(string, numberOfRepetition): # Add the argument order into the name of the function
    for i in range(numberOfRepetition):
        print(string)
printRepeatStringNumberOfRepetition("Hello World",3)