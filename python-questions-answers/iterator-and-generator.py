"""

An iterator is an object that implements the iterator protocol 
and provides an __iter__() method and a __next__() method.

A generator is a specific type of iterator that can be created 
using a function with the yield keyword. It allows you to yield 
values one at a time, making it memory-efficient.

"""

def my_generator():
    yield 1
    yield 2
    yield 3

for item in my_generator():
    print(item)

