import itertools

"""
#Infinite iterators example
"""

# 1. count()

for i in itertools.count(5, 5):
    if i == 35:
        break

    print(i, end =" ")

# 2. cycle()
count = 0

for i in itertools.cycle('AB'):
	if count > 7:
		break
	else:
		print(i, end = " ")
		count += 1



# 2.2 cycle()
l = ['Geeks', 'for', 'Geeks']

iterators = itertools.cycle(l)

for i in range(6):
	print(next(iterators), end = " ")



# 3. repeat()
	
print ("Printing the numbers repeatedly : ")
print (list(itertools.repeat(25, 40)))


'''
Combinatoric iterators
'''
# 1. product
from itertools import product
print(list(product(['a', 'b', 'c'], repeat = 2)))
print()

print("The cartesian product of the containers:")
print(list(product(['big', 'bazaar'], [2, 1])))
print()
   
print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

# 2. Permutations




import sys
sys.exit()
# Multiply of 2 lists using operator and map
# It takes less time as compare to loops
import operator
import time

# Defining lists
L1 = [1, 2, 3]
L2 = [2, 3, 4]
 
# Starting time before map
# function
t1 = time.time()
 
# Calculating result
a, b, c = map(operator.mul, L1, L2)

# Ending time after map
# function
t2 = time.time()
 
# Time taken by map function
print("L1 :", L1)
print("L2 :", L2) 
print("Result:", a, b, c)
print("Time taken by map function: %.6f" %(t2 - t1))
