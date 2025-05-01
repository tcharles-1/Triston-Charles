#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     19.6 problem 1
#
# Author:      tristonc
#
# Created:     04/30/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def readposint():
    while True:
        user_input = input("Please enter a positive integer: ")

        if user_input == "":
            print("You didn't enter anything.")
            continue

        try:
            number = int(user_input)

            if number > 0:
                return number
            else:
                print("The number must be greater than 0.")

        except ValueError:
            print("That is not a valid number.")

result = readposint()
print("You entered:", result)
