# # "Create a class called ToDoList
# # Allow the user to:
# # Add tasks
# # View tasks
# # Mark tasks as completed
# # Delete tasks
# # Store tasks in a .txt file."


import json

class ToDoList:

    def addData(self,name,task,status):
      
        f = open("toDoListTask.txt","r")
        data = f.read()
        f.close()
        if data:
            data = json.loads(data)
        else:
            data = {}    

        data[name]={}
        data[name]["Task"]=task
        data[name]["Status"]=status
        print(data)
        f = open("toDoListTask.txt","w")
        Finaldata = json.dumps(data, indent=4)
        f.write(Finaldata)
        f.close()

        print("Data added successfully.")

    def viewData(self):
        f = open("toDoListTask.txt","r")
        print(f.read())
        f.close()
        

    def updateData(self):

        updateName= input("Enter task no. whose data is to be updated : ")
        key = input("Enter the key:")
        updateStatus = input("Enter updated status : ")

        f = open("toDoListTask.txt","r")
        old_dict = f.read()
        f.close()
        data = json.loads(old_dict)
        data[updateName].update({key : updateStatus})
        print(data)
        updated_data = json.dumps(data, indent = 4)
        f = open("toDoListTask.txt", "w")
        f.write(updated_data)
        f.close()

    def deleteTask(self):
         updateName = input("Enter the task no. to be deleted : ")
         f = open("toDoListTask.txt", "r")
         data = f.read()
         f.close()
         data = json.loads(data)
         if data:
            data.pop(updateName)
            print(data)
            updatedData = json.dumps(data, indent = 4)
            f = open("toDoListTask.txt", "w")
            f.write(updatedData)
            f.close()
         else:
             print("NO DATA...!!")

    
toDo = ToDoList()
operation = input("Enter the task you want to perform(add, update, view, delete) : ")

while operation != "NO":
    if operation == "add":
        name = input("\nEnter task no : ")
        task = input("Enter task : ")
        status = input("Enter status : ")
        toDo.addData(name,task,status)
    elif operation == "view":
        toDo.viewData()
    elif operation == "update":
        toDo.updateData()
    elif operation == "delete":
        toDo.deleteTask()    
    else:
        print("Invalid Operation..") 

    operation = input("Enter the task you want to perform(add, update, view, delete) : ")
           













