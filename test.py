#!/usr/local/bin/python3.10

import sys

def func(*args, **kwargs):
    for x, y in kwargs.items():
        print(x, y)

func(d=1, c=3, b=10)

sys.exit()


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    pass
'''
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
'''





def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))




i = 5

def f(arg=i):
    print(arg)

i = 6
f()


def fib(n):    # write Fibonacci series up to n
   """Print a Fibonacci series up to n."""
   a, b = 0, 1
   while a < n:
       print(a, end=' ')
       a, b = b, a+b
   print()

f = fib
f(10)
fib(20)
fib(30)


# point is an (x, y) tuple
point = (1,3)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


def http_error(status):

    match status:
        case 400.100:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case 'hello':
            print("HELLO JI")
        case _:
            print("Something's wrong with the internet")


http_error(400.100)




import sys

for x in range(10):
    print(x)
    if x == 5:
        break
else:
    print("Done")








users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
#for user, status in users.copy().items():
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
