
#========================================================
# Value of x will not change without using nonlocal x
#========================================================
def func(y):
    x = y
    def inner():
        # This value will not change value of x outside
        # its scope
        x = 10
        
    inner()
    return x

print(func(2)) #will pring 2

#========================================================
# Value of x will change now using nonlocal x
#========================================================
def func(y):
    x = y
    def inner():
        nonlocal x
        x = 10
        
    inner()
    return x

print(func(1)) #will pring 10


#========================================================
# Using global keyword 
#========================================================
x = 5

# changing global value of x
def func(y):
    x = y
    def inner():
        # This will change global x
        global x 
        x = 10 
    inner()
    # This will return x local to function func
    return x  

print(func(2))
