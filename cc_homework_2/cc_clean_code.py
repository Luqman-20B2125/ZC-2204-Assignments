# Comment was removed as it's an added thing that needs to be maintained to be relevant but is not important
dateOfBirth = 3/12/2002

# Deleted function that is to do deleted and was commented out

# No more comment on places where it is unnecessary
# Comment is removed as the code is self explanatory
# Comment no longer contains misleading
def compareTwoNumbers(num1, num2): # This function compares two numbers and prints out which is greater than the other
    if (num1 > num2):
        print(num1, " is greater than ", num2)
    else:
        print(num2, " is greater than ", num1)

# Variable is now close to where it is used   
num1 = 10 
num2 = 11 
compareTwoNumbers(num1, num2)

# Spacing in between functions, easier to focus on closely related groups
# Warning exists
# Reason code exists is given
# This code exists for the purpose of an example of control variable outside of loop in bad code
# Control variable declared inside function where the loop exists instead 
# of having it as parameter and assigning a value to it in the function anyway
def decrementFrom1000To0(): # This function has no use to the project, its purpose is to just decrement a control variable 
                            # from 1000 to 0
    controlVar = 1000
    while controlVar > 0:
        controlVar -= 1

# Comment detailing changes to code and author of changes is removed as version control is able to handle this nowadays.

# Related code is near each other
# First dependent function, function that calls the other function is now above it
# Comment gives info on why something is done
def quickSort(array, low, high, n):
    if low < high:
        j = partition(array, low, high, n) # calls partition which partitions the array into smaller and bigger values on one side
        quickSort(array, low, j, n)        # calls itself to now sort the smaller partition as it may not necessarily 
                                           # be properly sorted on the smaller partition for example it may be 1, 5 , 4 on the smaller side
        quickSort(array, j + 1, high, n)   # same reason as previous call but for the bigger partition side
    return array

# Second dependent function, function that is being called is now below the caller
# Unnecessary spacing in between the lines of code removed
# Comment why code is used exists
def partition(array, low, high, n): # This function partitions an array,
                                    # then sorts the smaller values to the left side of partition and bigger to the right side
                                    # finally return value of where the partition is at
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