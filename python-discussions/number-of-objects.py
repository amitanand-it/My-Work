# ON TERMINAL VALUE RANGE IS -5 TO 256 ONLY
# BUT IN VISUAL STUDIO EXCEPTING BIGGER VALUES
a = 30000000000 
b = 30000000000 
print(a is b)
print(id(a), id(b))



a = 1
b = 1
# AT THIS LEVEL GLOBALS AND LOCALS WILL BE SAME

def func():
    c=10
    d=10
    e=10
    print(globals())
    print(locals())
    print(c is d)
    print(c is e)

func()
"""
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f84b587fca0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/tradeindia/mywork/python-discussions/number-of-objects.py', '__cached__': None, 'a': 1, 'b': 1, 'func': <function func at 0x7f84b58d2f70>}

{'c': 10, 'd': 10, 'e': 10}
"""


# IMPORTANT MAGICAL VARIABLES 
# __name__ , __file__, __annotations__

# TOTAL OBJECTS CREATED FOR VARIABLES ONLY
# [4] IF A AND B ARE BETWEEN RANGE -5 AND 256 ELSE [5]