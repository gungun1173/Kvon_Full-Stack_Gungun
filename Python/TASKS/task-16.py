import json
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def insert_details(self):
        thisdict = {}
        thisdict["Name"] = self.name
        thisdict["Age"] = self.age
        thisdict["Salary"] = self.salary
        thisdict = json.dumps(thisdict)
        f = open("employee-2.txt","a")
        f.write(thisdict)
       

task = input("Do You want to continue the task(YES/NO):")
while task != "NO":
    Name = input("Enter the name of the Employee:")
    Age = int(input("Enter the age:"))
    Salary = int(input("Enter the salary:"))
    e1 = Employee(Name, Age, Salary)    
    e1.insert_details()    
    f = open("employee-2.txt", "r")
    print(f.read())
    task = input("Do You want to continue the task(YES/NO):")