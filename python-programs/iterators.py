# Iterable Objects are tuples, lists, dicts, str
#from msilib.schema import Error


t = (3,5,1)
# get iterator 
t = iter(t)
print(next(t))
print(next(t))
print(next(t))

# Iter with string
# Need to notice like generator it is not a function
mystr = "banana"
myit = iter(mystr)
for x in myit:
    print(x)

# create own iterator
class Adder():

    def __init__(self, end, step=1, start=1):
        self.start = start 
        self.end = end 
        self.step = step 

    def __iter__(self):
        self.a = self.start 
        return self

    def __next__(self):
        if self.a > self.end:
            raise StopIteration("No more iterations can be done")

        curr_value = self.a
        self.a += self.step 
        return curr_value 

add2 = Adder(step=2, start=1, end=30 )
iter_obj = iter(add2)
for x in iter_obj:
    print("=>", x)

add3 = Adder(step=3, start=0, end=30 )
iter_obj = iter(add3)
for x in iter_obj:
    print("=>", x)


