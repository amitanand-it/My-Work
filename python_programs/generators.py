# checking generator using obj method
def demo():
    yield 1
    yield 2
    yield 3

gen = demo()
print(gen.__next__())
print(next(gen))
print(next(gen))

print("********************************")
def squares(n):
    for x in range(1,n+1):
        yield x, x**2

for x in squares(5):
    print(x)


print("********************************")
# generator using paranthesis
# after finishing first print statement iterations done , next will not work
cubes = ( (x, x**3) for x in range(1, 5))
print(tuple(cubes))
print(dict(cubes))
print(list(cubes))

print("********************************")
# fibonacci series 
def fib(n):
    if n == 0: yield 0
    if n == 1: yield 1
    a, b = 0, 1
    for x in range(n):
        yield a
        a, b = b, a+b

n = 10
print(f"Fibonacci Series till {n}")
for x in fib(n):
    print(x, end=' ')
print()



def demo2():
    yield 1
    yield 2
    yield 19

#gen = demo2()
for x in demo2():
    print(x)
