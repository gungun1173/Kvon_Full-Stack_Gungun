# Create a Shape Class:
# Parent Class: Shape → Method: area()
# Child Classes:
# Rectangle → Area = l*b
# Circle → Area = π*r²


class Shape:
    def __init__(self, name):
        self.name = name
       

    def display_area(self, area):
        print(f"Area of {self.name} is {area}/per sq. unit")    

class Rectangle (Shape):
    def __init__(self, name, l, b):
        super().__init__(name)
        self.l = l
        self.b = b

    def area(self):
        return  self.l * self.b   

class Circle (Shape):
    def __init__(self, name, r):  
        super().__init__(name) 
        self.r = r     

    def area(self):
        return 3.14 * self.r * self.r


rect = Rectangle("rectangle", 3, 4)
rect_area = rect.area()
rect.display_area(rect_area)

circle = Circle("circle", 2)
circ_area = circle.area()
circle.display_area(circ_area)






























