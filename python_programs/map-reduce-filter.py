
def greet(name):
    return "Hello, {}!".format(name)

def print_greeting(f, n):
    print(f(n))

print_greeting(greet, 'Amit Anand')
# MAP , REDUCE AND FILTER DO SAME THING
import math
print(list(map(math.sqrt, [4,25,3])))

# import operator
# print(list(map(operator.add, [4,25,3])))

def youth(age):
    if age < 18: return True

print(list(filter(youth, [18, 19, 10, 29 , 17])))
print(list(filter(lambda x: x < 18, [18, 19, 10, 29 , 17])))


from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))

import operator
print(reduce(operator.add, ([1,2,3,4,5], [5,6,7,8], [1,2,3,4])))
print(reduce(operator.mul, [1,2,3,4,5]))
print(reduce(operator.mul, range(1,6))) # Factorial
print(reduce(lambda x,y: x if x > y else y , ([1,2,3,4,15, 5,6,7,8])))
print(reduce(lambda x,y: x+y , range(1,11))) # Fibonacci Result

print("Fibonacci program")
from itertools import accumulate
print(*[x for x in accumulate(range(11),operator.add )])



print(reduce(operator.mul, range(1,6), 3))

l = [(1,2,3), (4,5,6)]
print(l,list(zip(*l)), sep='\n')
print(list(map( lambda x: x.count(1) , zip(*l) )))







    