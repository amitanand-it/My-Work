
from imp import init_builtin

"""
Q. Is this possible to make a decorator which can reverse the functionality
of in-built function str.upper to str.lower
"""

def greet(func):

    def inner():
        print("Hello, ", end=' ')
        func()

    return inner

upper = greet(str.upper)

print(upper("amit"))