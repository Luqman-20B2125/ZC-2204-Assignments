n = "Luqman" # Name is not informative, only a single letter so need to mentally map its meaning every time we see it

flagBool = 0 # Name spreads disinformation

l, O = 0, 0 # Using l or O for variable names as they look like 1 and 0 respectively, so might confuse people reviewing the code.
if l == 0: 
    print("1 is", O)

schoolString = "Primary" # Different names but same implied meaning and redundant naming
schoolNameString = "Stella School"

fName, FName = "John", "John Smith"  # Similar names that does not distinguish the content of the variables.

fMLN = "John Devan Smith"# Unpronouncable name

dtOfExm = "22/3/2022" # Unsearchable name

iMoneyAmount = 1000 # Encoding the name to indicate variable type, in this example we use i to indicate integer

class Apply: # Naming a class using a verb
    def __init__(self, data = None):
        self.data = data

def Book(): # Naming a function using a noun
    print("Book")

def TrumanShow(): # Naming a function using a cultural reference rather than its direct use
    print("Hello World!")

def AddTwoIntegers(int1, int2): # Using different words for the same effect on different functions or classes
    m_sum = int1 + int2         # Using prefix to indicate variable being a member of a function or class
    return m_sum

def SumTwoFloats(float1, float2):
    m_sum = float1 + float2
    return m_sum

itemCatalogue = ["Banana","Apple","Coconut"] # Using names that could instead use programming technical terms

city, country = "Bandar Seri Begawan", "Brunei Darussalam" # Using names that do not have the context needed to give meaning

def checkBool(flag): # functions that do multiple jobs and those with boolean as an argument,
                     # as boolean means it will do multiple jobs
    if flag == True:
        print("Flag is True")
    else:
        print("Flag is False")
checkBool(True)

def printRepeat(string, numberOfRepetition):# Function with two arguments with no indication of argument order
    for i in range(numberOfRepetition):
        print(string)
printRepeat("Hello World",3)