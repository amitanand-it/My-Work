# Enter your code here. Read input from STDIN. Print output to STDOUT

a = map(int, (input()).split())
b = map(int, (input()).split())

from itertools import product
s = ''
for t in product(a,b):
    s =  s + ' ' + str(t)
print(s.strip())