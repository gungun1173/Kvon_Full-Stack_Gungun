
# TASK-5 Function taking list of Numbers as Arguments and returning a list containing only even numbers
def even_num(values):
    newlist = [x for x in values if x % 2 == 0]
    return newlist

print("\n\nFunction to extract even numbers list from original list:")
print("Original List:",[101,2,11,22,54,31,0,112,72] )
print("List containing Even numbers:",even_num([101,2,11,22,54,31,0,112,72]), "\n\n")   



# TASK-6 Function Returning Reverse String without using the built in functions
def reverse_str(str1):
    i = len(str1) - 1
   
    
    while i >= 0:
        print(str1[i], end="")
        i = i - 1
   
print("Reversing a string function:")   
print("python Tutorials")
reverse_str("python Tutorials")    
