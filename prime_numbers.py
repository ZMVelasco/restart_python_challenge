# Version: 3.0
# Coding: utf-8
# This program will print the prime numbers from a given range, it could be any range between 1 and 1000, for example 1-250.

from colored import Fore, Back, Style

# Creating color variables
plum = Fore.PLUM_1
turquoise = Fore.MEDIUM_TURQUOISE
blue = Fore.SKY_BLUE_2
pink = Fore.HOT_PINK_2
pink_2 = Fore.HOT_PINK_3B
pale_violet_red = Fore.PALE_VIOLET_RED_1
red = Fore.INDIAN_RED_1B
reset_color = '\x1b[0m'

print(plum + "You can choose a range between 1 and 1000, for example 1-250, from which you will get all the prime numbers." + reset_color)

# This function will ask the user to input the range, it will check if the range is valid and it will return the range.
def ordered_range():
    while True:
        smaller_number = int(input(turquoise + "Enter the smaller number: " + reset_color))
        bigger_number = int(input(turquoise + "Enter the bigger number: " + reset_color))

        if smaller_number < 1 or bigger_number > 1000:
            print(red + "The range is not valid, please try again." + reset_color)
            continue
        elif smaller_number > bigger_number:
            print(red + "The range is not valid, the first number should be smaller than the second one." + reset_color)
            continue
        else:
            break
    return smaller_number, bigger_number

smaller_number, bigger_number = ordered_range()
print(pink + "The range you picked is " + pale_violet_red + f"{smaller_number} - {bigger_number}" + reset_color)

# This function will get the prime numbers from the range the user picked and it will save them in a file called prime_numbers.txt.
def get_prime_numbers(smaller_number, bigger_number):
    with open("prime_numbers.txt", "w") as file:
        file.write(f"These are all the prime numbers from the range you picked:\n")
        for number in range(smaller_number, bigger_number + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    print(pink_2 + str(number) + reset_color)
                    file.write(f"{number}\n")

print(blue + "These are all the prime numbers from the range you picked:" + reset_color)
get_prime_numbers(smaller_number, bigger_number)
print(blue + "The resulting prime numbers have been saved in a file called prime_numbers.txt" + reset_color)
