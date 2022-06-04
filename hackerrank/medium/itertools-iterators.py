from itertools import permutations
from itertools import combinations

n = int(input()) 
letters = input().split()[:n]
n_indices = int(input()) 

total_count = 0
match_count = 0
perm_list = list(combinations(letters,n_indices))

for t in perm_list:
    if 'a' in t:
        match_count += 1
    total_count += 1
         
print(round(match_count/total_count,3))


"""

from itertools import permutations
from itertools import combinations

# input = 'a c a d'
input = 'a b c a d b z e o'

n = 9 
letters = input.split()[:n]
n_indices = 4 
# n = 4 
# letters = input.split()[:n]
# n_indices = 2  

indices = [ i for i, x in enumerate(letters[:n_indices], start=1) if x == 'a' ] 
print(indices)

perm_list = list(combinations(range(1,n+1),n_indices))
print(perm_list)

total_count = len(perm_list)
print(total_count)

# contains_a =  [ t for t in perm_list if 'a' in t ]
# print(contains_a)
# contains_indices = [ x for x in indices for y in perm_list if x in y  ]
contains_indices = []
[ contains_indices.append(y) for x in indices for y in perm_list if x in y and y not in contains_indices ]

print(contains_indices)


res = len(contains_indices) / total_count
print(res)
"""

"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Constraints



All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is .
"""