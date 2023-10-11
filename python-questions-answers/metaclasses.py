# Type of all the structure is class type
for x in (list, tuple, dict, set):
    print(x, type(x))

class Foo:
    pass

print("Type of Foo: ", type(Foo))


# Types of objects 
for x in ([1], (1,), {1:2}, {1}):
    print(x, type(x))


# USING TYPE CREATING DYNAMIC CLASS
# HERE Foo is class name , second arg is for superclasses tuple, thire arg is for attributes
Foo = type('Foo', (), {})
x = Foo()
print(x, type(x))


Bar = type('Bar', (Foo,), dict(attr=100))
x = Bar()
print(x.attr)

