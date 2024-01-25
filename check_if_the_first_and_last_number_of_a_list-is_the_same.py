# Assignment 5 - Exercise 5
# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

# Compare if the first and last number in the list is the same

def first_and_last_comparison(numberList):
    print("Given List: ", numberList)
    
    first_number = numberList[0]
    last_number = numberList[-1]

    same = first_number == last_number
    return same

# Print based on the given