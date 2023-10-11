"""
Closures are nested functions that capture and remember values 
from their enclosing lexical scope, even if that scope is no 
longer available. They are often used to create function factories 
or for encapsulation.
"""

def outer_function(x):

    def inner_function(y):
        return x + y

    return inner_function



add_5 = outer_function(5)
result = add_5(10)
print(result)  # Output: 15

result = (outer_function(10))(20)
print(result)  # Output: 30 

