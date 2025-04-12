# "File Handling Task:
# Create a text file called students.txt
# Allow user to enter Name, Age, Marks and save in file.
# Read and display file contents.


import json
task = input("Do you wnat to continue the task (YES/NO):")
while task != "NO":
    f = open("students.txt", "a")
    thisdict = {}
    Name = input("Enter the Name of the user:")
    Age = int(input("Enter the Age of the user:"))
    Marks = int(input("Enter the marks:"))
    thisdict["Name"] = Name
    thisdict["Age"] = Age
    thisdict["Marks"] = Marks
    thisdict = json.dumps(thisdict)
    f.write("\n", thisdict)
    f = open("students.txt", "r")
    print(f.read())
    task = input("Do you wnat to continue the task (YES/NO):")