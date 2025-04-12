# printing random numbers
import random

print(random.randrange(1,10))

#len() function
a = "Hello, World!!"
print(len(a))

# for loop
str = "we live in rainbow of chaos"
for s in str:
    print(s)

# in function
text = "we live in rainbow of chaos"
print("chaos" in text)

# Multiline Strings
txt = """
        we live in rainbow of chaos
        to chill
        feeling clumsy
        an apple a day keeps the doctor away.
        """
print(txt)
print(text.upper())
print(text.lower())

# Strip() function
a = "  Hello, World!!     "
print(a, len(a))
b = a.strip()
print(b, len(b))

# f-strings
age = 34
b = f"Age is just a number and the number is {age}"
print(b)
b = "Age is just a number and the number is {age:}"
print(b.format(age=34))

# Escape Character
txt = "we are the so called \"ALPHA\" Generations."
print(txt)
print(txt.capitalize())
print(txt.casefold())
text1="banana"
print(text1.center(20, "0"))



