#  "Create a Student Class:
# Attributes: Name, Roll Number, Marks
# Methods:
# get_details() → Print name, roll number, marks
# is_passed() → Check if marks > 33 then passed else failed

class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def __str__(self):
       return f"\nStudent name : {self.name} \nroll numbers : {self.roll_num} \nmarks : {self.marks}"

    def is_passed(self):
        if self.marks > 33 :
            print(self.name + " has 'PASSED' the Examination")
        else :
            print(self.name + " has 'FAILED' in the Examination")    

resume = input("do you want to resume the task (YES/NO) :")

while resume != "NO" :
    name = input("Enter the name of the user:")
    roll = input("enter the roll number:")
    marks = int(input("Enter the marks:"))
    s1 = Student(name, roll, marks)
    print(s1)
    s1.is_passed()

    resume = input("\ndo you want to resume the task (YES/NO) :")







