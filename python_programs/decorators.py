"""
Q. Is this possible to make a decorator which can reverse the functionality
of in-built function str.upper to str.lower
"""



def lower_it(func):

    def wrapper():
        res = func()
        return res.lower()
    
    return wrapper

def split_string(func):

    def wrapper():
        s = func()
        return s.split()
    return wrapper

@split_string
@lower_it
def hello():
    return "hEllo AmiT"

print(hello())



"""
def greet(func):

    def inner():
        print("Hello, ", end=' ')
        func()

    return inner

upper = greet(str.upper)

print(upper("amit"))
"""