import random

number = random.randrange(1, 100)
print(number)
value = int(input("Enter the number:"))

if value == number:
     print("You guessed it right!!")
else:
    while value != number:
        value = int(input("Enter the number:"))
        if value == number:
            print("You guessed it right!!")
            break

    


