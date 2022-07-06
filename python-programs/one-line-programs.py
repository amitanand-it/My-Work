# reverse string
s[::-1]  

#palindrome
s == s[::-1]  

#factorial
math.factorial(3) 

#factorials in a list
map(math.factorial, range(9)) 

#cubes in a list
map(lambda x: (x, x**3) , range(9))

# sum of the provided tuples in a list
list(map(lambda x: sum(x) , [(1,3), (5,3)]))

# converting to float only if list has valid float strings 
list( map( float, filter( lambda x: re.match('\d(.\d+)?', x) , ["12.3", "3.3", "a"])))

# gettig square root of all the positive integers only
list(map(math.sqrt, filter(lambda x: x>=0, [25, 9, 81, -16, 0])))

# getting minimum/maximum/sum number from a list
sum([10, 11, 2, 3, 4])
min([10, 11, 2, 3, 4])
max([10, 11, 2, 3, 4])

all([10, 11, 2, 3, 4, 0])
any([10, 11, 2, 3, 4, 0])



