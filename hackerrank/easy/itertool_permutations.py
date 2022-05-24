from itertools import permutations
from math import perm

#print(list(permutations([1,3,2], 2)))
s, n = (input()).split()
#s = 'HACK 2'
s = s.replace(' ', '')
data = list(permutations(s, int(n)))
for x in sorted(data):
    print(''.join(x))

