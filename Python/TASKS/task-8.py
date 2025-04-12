
# Create a program that manages a dictionary of students with their marks and allows the user to search, add, and update student records.

def search_record(value) :
    print("\n", thisdict[value], "\n\n")

def add_record(key, value):
    thisdict[key] = value  
    print("\n\n",thisdict,"\n\n")
 


def update_record(key, value) :
    thisdict.update({key : value})
    print("\n\n",thisdict,"\n\n")

def show_record():
    print("\n\n",thisdict,"\n\n")
  


thisdict = {
    "Gaurav" : 80,
    "Shreya" : 56,
    "Sourav" : 78,
    "Vishakha" : 90
}

task = input("Enter the Operation to be Performed (show, add, update, search):")
while task != "Exit" :

    if task == "add" :
        key = input("enter the key:")
        value = int(input("enter the value to be added:"))
        add_record(key, value)
       
    elif task == "search" :
        value = input("Enter the value to be searched:")
        search_record(value)  

    elif task == "update":
        key = input("enter the key:")
        value = int(input("enter the value to be updated:")) 
        update_record(key, value)

    else:
        show_record()    

    task = input("Enter the Operation to be Performed (show, add, update, search):")

    



