# Assignment 5 - Exercise 5
# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

# Compare if the first and last number in the list is the same

def first_and_last_comparison(numberList):
    print("\nGiven List: ", numberList)
    
    first_number = numberList[0]
    last_number = numberList[-1]

    same = first_number == last_number
    return same

# Print based on the given

numbers_x = [10, 20, 30, 40, 10]
print("Result is", first_and_last_comparison(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Result is", first_and_last_comparison(numbers_y))