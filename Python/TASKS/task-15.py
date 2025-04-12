# Exception Handling Task:
# Create a Python program that:
# Asks the user for 2 numbers.
# Performs division.
# Handle ZeroDivisionError and ValueError.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num2 == 0:
    raise ZeroDivisionError("Denominator Value cannot be Zero")
elif not type(num1) is int or not type(num2) is int:
    raise ValueError("Invalid Value Type Entered")
else:
    result = num1 / num2
    print("division of two numbers is:", result)