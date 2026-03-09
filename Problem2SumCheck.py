# Barakat Owoalade
# March 9 2026
# This program asks the user for two numbers and checks if the sum is greater than 10, less than 10, or equal to 10

def check_sum():

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    total = number1 + number2

    if total > 10:
        print("The sum is greater than 10")

    elif total < 10:
        print("The sum is less than 10")

    else:
        print("The sum is equal to 10")


check_sum()
