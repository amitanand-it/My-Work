import math
from wsgiref.simple_server import WSGIRequestHandler 

arr =[3,2,4,5,1]

l = list()

for x in arr:
    for y in arr:
        if x+y == 6 and (y,x) not in l and x!= y:
            l.append((x, y))

print(l)



import sys
sys.exit()

from itertools import combinations

arr =[3,2,4,5,1]
for x, y in list(combinations(arr, 2)):
    if x+y == 6:
        print((x,y))











#print (list(combinations('12345',2)))

A = [1,1,3,3,3]
#print(list(combinations(A,4)))

s = sorted('HACK')
print(list(combinations(s,1)))
print(list(combinations(s,2)))


# INPUT =>  'HACK 2'

from itertools import combinations
s, n = input().split()
s = sorted(s)
com_list=[]
for k in range(int(n)):
    for y in ((combinations(s,k+1))):
        com_list.append(''.join(y))

for l in (sorted(com_list, key=lambda item: (len(item), item[0]))):
    print(l)