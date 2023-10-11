
class Book:

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __repr__(self):
        return f"Book(name='{self.name}', pages={self.pages})"
    
    def __add__(self, other):
        # Adding 2 Book objects should return Book object
        return Book(
                name = self.name + '-' + other.name, 
                pages = self.pages + other.pages, 
        )

b1 = Book(name='B1', pages=50)
b2 = Book(name='B2', pages=150)
b3 = b1 + b2
print(b3)

#print(b3 == eval(repr(b3)))  NOT MATCHING NEEDS TO BE CHECKED


"""
Some Examples of Dunder methods
a) Dictionary:

__getitem__: Used to access items using square brackets.
__setitem__: Used to set items using square brackets.
__delitem__: Used to delete items using square brackets.
__len__: Used to get the length of the dictionary.
b) List:

__getitem__: Used to access items using square brackets.
__setitem__: Used to set items using square brackets.
__delitem__: Used to delete items using square brackets.
__len__: Used to get the length of the list.
__iter__: Used to define custom iteration behavior.
__reversed__: Used to define custom reverse iteration behavior.
c) Class Objects:

__init__: Constructor method for object initialization.
__str__: Used for converting an object to a string (e.g., str(obj)).
__repr__: Used for a formal string representation of the object.
__eq__: Used for equality comparisons (e.g., obj1 == obj2).
__lt__: Used for less than comparisons (e.g., obj1 < obj2).
__le__: Used for less than or equal comparisons (e.g., obj1 <= obj2).
__gt__: Used for greater than comparisons (e.g., obj1 > obj2).
__ge__: Used for greater than or equal comparisons (e.g., obj1 >= obj2).
"""
