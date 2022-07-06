import sys
import math

import re

txt = "amit Hello amit Hi amit Ji"
m = re.finditer(r"amit", txt)
print(m)

sys.exit()


def timeConversion(s):
    # Write your code here
    tt, am_pm = s[:-2], s[-2:]
    hh, mm, ss = tt.split(":")

    if am_pm == 'PM':
        hh = int(hh)
        if hh != 12 and hh >= 1:
            hh += 12
        return f"{hh}:{mm}:{ss}"
    
    if am_pm == 'AM':
        if hh == "12":
            hh = '00'

        return f"{hh}:{mm}:{ss}"
    

s = "12:00:00AM"
s = "12:00:01AM"
s = "12:00:00PM"
s = "11:30:00PM"
print(timeConversion(s))




# print(sum(x for x in range(6)))


sys.exit()
degree_sign = u'\N{DEGREE SIGN}'
print(f"{int(math.degrees(math.atan(1)))}{degree_sign}")



import numpy
a = numpy.array([1,2,3,4,5][::-1], float)
print(a)



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