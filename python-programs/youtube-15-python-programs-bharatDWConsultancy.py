# 1. print prime numbers between 100 and 200

def isPrime(n):

    for x in range(2, n):
        if n%x == 0:
            return False 

    return True 

#print(list(filter(isPrime, range(100, 200) )))

#2. Sort functions to sort the elements in the list

l = [4,4,1,6,11,98]
l.sort()
#print(l)

l.sort(reverse=True)
#print(l)


#3. Sort functions to sort the elements in the list without using sort and sorted
def sort_list(data, reverse=False):
    data = data.copy()

    sorted_list = []

    while data:
        min = data[0]
        for x in data:
            if x < min:
                min = x

        if reverse == True:
            sorted_list.insert(0, min)
        else:
            sorted_list.append(min)

        data.remove(min)

    return sorted_list

l = [4,4,1,6,11,98]
#print(sort_list(l, reverse=False))
#print(sort_list(l, reverse=True))

# 4. Fibonacci Series using recursion
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-1) + fib(n-2)

#print(list(map(fib, range(10))))

# 5. Fibonacci Series using without recursion
def fib(n):

    if n == 0 : return 0
    if n == 1 : return 1

    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b 

    return a

print(list(map(fib, range(11))))
#print(fib(5))
        
