#Build a to-do list application using a dictionary where users can add tasks, mark them as completed, and view pending/completed tasks.

def search_record(value) :
    print("\n", thisdict[value], "\n\n")

def add_record(key, value, record):
    thisdict[record][key] = value  
    for x in thisdict :
        print(x)
        print(thisdict[x])
 


def update_record(key, value, record) :
    thisdict[record].update({key : value})
    for x in thisdict :
        print(x)
        print(thisdict[x])

def show_record():
    for x in thisdict :
        print(x)
        print(thisdict[x])
       
  


thisdict = {
    "Task-1":{
        "Name" : "Homework",
        "Status" : "Completed" 
    }, 
    "Task-2" : {
        "Name" : "Python_Tutorials",
        "Status" : "Pending"
    },
    "Task-3" : {
        "Name" : "DSA",
        "Status" : "Pending"
    },
    "Task-4" : {
        "Name" : "Semester Notes",
        "Status" : "Completed"

    },
    "Task-5" : {
        "Name" : "SQL Cheatsheet",
        "Status" : "Pending"
    }

}

task = input("Enter the Operation to be Performed (show, add, update, search):")
while task != "Exit" :

    if task == "add" :
        record = input("Enter the Task Name:")
        key = input("enter the key:")
        value = input("enter the value to be added:")
        add_record(key, value, record)
       
    elif task == "search" :
        value = input("Enter the value to be searched:")
        search_record(value)  

    elif task == "update":
        record = input("Enter the Task Name:")
        key = input("enter the key:")
        value = input("enter the value to be updated:")
        update_record(key, value, record)

    else:
        show_record()    

    task = input("Enter the Operation to be Performed (show, add, update, search):")

    



