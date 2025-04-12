def multiply(a,b):
    print(f"Multiplication of {a:} and {b:} is {(a*b):}")

def addition(a,b):
    print(f"Addition of {a:} and {b:} is {(a+b):}")

def subtraction(a,b):
    print(f"Subtraction of {a:} and {b:} is {(a-b):}")

def division(a,b):
    print(f"Division of {a:} and {b:} is {(a/b):}")      

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
operation = input("Enter the Operation to be Performed (multiply, addition, subtraction, division):")



if operation == "multiply":
    multiply(x,y)

elif operation == "addition":
    addition(x,y)

elif operation == "subtraction":
    subtraction(x,y)

else:
    division(x,y)    