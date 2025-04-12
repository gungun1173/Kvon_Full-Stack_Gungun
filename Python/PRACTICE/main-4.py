pi = 'global scope variable'
def outer():
    pi = 'outer scope variable'
    print(pi)
    def inner():
        nonlocal pi
        print(pi)
    inner()
outer()
print(pi)    
