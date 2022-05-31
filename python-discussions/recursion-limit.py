
def func():
    pass
    func()

# func()

# THIS PROGRAM WILL THROW BELOW ERROR
# RecursionError: maximum recursion depth exceeded

import sys
# MAXIMUM RECURSTION DEFAULT DEPTH IS 1000 
print(sys.getrecursionlimit()) # Prints 1000

# THIS LIMIT CAN BE CHANGED
sys.setrecursionlimit(2000) 
print(sys.getrecursionlimit()) # Prints 2000

# SAFE WAY TO SET RECURSION LIMIT BY CREATING A CONTEXT MANAGER
# Ref: https://www.codingem.com/python-maximum-recursion-depth/#:~:text=Python%20uses%20a%20maximum%20recursion,and%20infinite%20recursions%20are%20possible.
import sys

class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)

def fibonacci(n):
    if n == 1: return 0
    if n == 2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

with recursion_depth(2000):
    print(fibonacci(1000))


