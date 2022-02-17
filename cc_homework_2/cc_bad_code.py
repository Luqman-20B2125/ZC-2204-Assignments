# Comment separated from its original line due to addition or modification of code
dateOfBirth = 3/12/2002 

# Variable declared far from where it is used
# Commenting on everything causing the code to look cluttered
num1 = 10 # This variable contains the number 10 which is the first number of the two we want to compare with each other
num2 = 11 # This variable contains the number 11 which is the second number of the two we want to compare with each other

# Dependent function far from each other
# First dependent function, function that is being called is above the one that is calling it
# There is spacing between the lines of code that are in the same group for no reason making them seem less related
# No comment telling the reason of using this code or clarifying the meaning of the obscure code
def partition(array, low, high, n):

    pivot = array[low]

    i = low

    j = high

    while i < j:

        while i < n and array[i] <= pivot:

            i += 1

        while j >= 0 and array[j] > pivot:

            j -= 1

        if i < j:

            array[i], array[j] = array[j], array[i]

    array[low], array[j] = array[j], array[low]

    return j

# To do comment for removing bad or useless code
# Code that is commented out instead of deleted
#def bubbleSort(array): # To do: Remove bubbleSort now using quicksort as quicksort is faster.
#    for i in range(len(array) - 1, 0, -1):
#        for j in range(len(array) - 1, len(array) - 1 - i, -1):
#            if array[j] < array[j - 1]:
#                array[j], array[j - 1] = array[j - 1], array[j]
#    return array


# Comment explaining what code does instead of making a function with a name that says what it does
# Comment is redundant, code is descriptive enough without the comment
# Comment contains misleading information
# Variable we declared at the top is used here
if (num1 > num2): # This group of code compares two numbers and returns us which of the two is greater.
    print(num1, " is greater than ", num2) # prints out num1 is greater than num2, 
                                           # with the actual value inside of variable not num1 and num2
else:
    print(num2, " is greater than ", num1) # prints out num2 is greater than num1, 
                                           # with the actual value inside of variable not num1 and num2

# No spacing in between groups that aren't closely related making it harder to read
# No warning of why not to run
# No info on why this code exists
# Control variable declared outside of loop it is used in
controlVar = 1
def decrementFrom1000To0(controlVar):
    controlVar = 1000
    while controlVar > 0:
        controlVar -= 1
# Comment detailing the changes to the code and when it was done
# Comment telling us the creator of code
# Changed on 1/2/2022 Joined the project
# Changed on 5/2/2022 Added a new function to the code
# Changed on 11/2/2022 Function removed as it was not needed
# Changed on 13/2/2022 Added to do comment on bubbleSort function to remove it
# Changed on 19/2/2022 Commented out bubbleSort function
# By Luqman(20B2125)
# Related code is separated from each other
# Second dependent function, function that is calling is below the one that is calling it
# Comment gives info but not enough to make sense
def quickSort(array, low, high, n):
    if low < high:
        j = partition(array, low, high, n) # Partitions the array
        quickSort(array, low, j, n)        # calls itself
        quickSort(array, j + 1, high, n)   # calls itself again
    return array

# Comment that was separated
# This line of code is the date of birth of a person