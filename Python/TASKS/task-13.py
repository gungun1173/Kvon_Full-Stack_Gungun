# Operator Overloading:
# Create a class Book with price attribute.
# Overload + operator to add the price of two books."

class Book:
    def __init__(self, x):
        self.x = x

    def add_price(self, other):
        x = self.x + other.x  
        return Book(x)

price_1 = int(input("Enter the price for Book-1:"))    
p1 = Book(price_1)
price_2 = int(input("Enter the price for Book-2:")) 
p2 = Book(price_2)
p3 = p1.add_price(p2)
print("Adding price of both Books:", p3.x)