"""

Given  sets of integers,  and , print their 
symmetric difference in ascending order. 
The term symmetric difference indicates those values that 
exist in either  or  but do not exist in both.

"""
n1 = int(input())
set_a = set(map(int, input().split()))
n2 = int(input())
set_b = set(map(int, input().split()))

# print(set_a, set_b)


for _ in sorted(set_a.union(set_b) - set_a.intersection(set_b)):
    print(_)

