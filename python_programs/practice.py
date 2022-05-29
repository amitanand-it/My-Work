import sys
import numpy
a = numpy.array([1,2,3,4,5][::-1], float)
print(a)


sys.exit()

class A():

    __instance = None

    def __init__(self):
        if A.__instance == None: 
            A.__instance = self
        else:
            raise Exception("ERROR ")

    def get_instance(self):
        if A.__instance == None:
            A() 
        return A.__instance



a = A()
b = A()
print(a)
print(b)
#b = A()




sys.exit()
from operator import indexOf

import sys
class Chr():

    alphabets= 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, ch, n):
        self.n = n  
        self.ch = ch 
        self.index = Chr.alphabets.index(ch)

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index + self.n % len(Chr.alphabets) - 1
        self.ch =  Chr.alphabets[index]
        self.index = index 
        print(self.ch)

        
obj = Chr('c', 3)
inc = iter(obj)
print(next(inc))
print(next(inc))


sys.exit()
class Inc():

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x 
        
obj = Inc()
inc = iter(obj)
for x in range(10):
    print(next(inc))



sys.exit()
alphabets='abcdefghijklmnopqrstuvwxyz'
ch ='x'
ind = alphabets.index(ch)
ind += 3
new_ch = alphabets[ind]
print()