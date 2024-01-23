# Version: 3.0
# Coding: utf-8

# This program will print the prime numbers from a given range, it could be any range between 1 and 1000, for example 1-250.
print("You can choose a range between 1 and 1000, for example 1-250, from which you will get all the prime numbers.")

def ordered_range():
    smaller_number = int(input("Enter the smaller number: "))
    bigger_number = int(input("Enter the bigger number: "))
    if smaller_number < 1 or bigger_number > 1000:
        print("The range is not valid, please try again.")
        ordered_range()
    elif smaller_number > bigger_number:
        print("The range is not valid, the first number should be smaller than the second one.")
        ordered_range()
    else:
        return smaller_number, bigger_number

smaller_number, bigger_number = ordered_range()
print(f"The range you picked is {smaller_number} - {bigger_number}")


