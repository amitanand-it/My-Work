# # Correct Solution
# Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

# For the first word in group B, 'a', it appears at positions  
# and  in group A. The second word, 'c', does not appear in group A, so print .

# Expected output:

# 1 3
# -1

from collections import defaultdict

n, m = map(int,input().split())

a = defaultdict(list)
for i in range(1, n + 1):
    a[input()].append(i)

for i in range(1, m + 1):
    key = input()
    if len(a[key]) > 0:
        print(" ".join(str(c) for c in a[key]))
    else:
        print(-1)

# ======================================================


from collections import defaultdict

def process(list_a, list_b):
    unique = []
    for x in list_b:
        if x not in unique:
            unique.append(x) 

    d = defaultdict(list)
    for x in unique:
                
        if x not in list_a:
            print("-1")
        
        for i, y in enumerate(list_a):
            if x == y:
                d[x].append(i+1)

        print(' '.join(map(str, d[x])))
        
        

if __name__ == '__main__':
    #a, b = map(int, input().split())
    # list_a = []
    # list_b = []
    # for x in range(a):
    #     list_a.append(input())
        
    # for x in range(b):
    #     list_b.append(input())

    list_a = [3, 3, 1, 2, 3, 1, 2]
    list_b = [3, 3, 1, 2, 3, 1, 2, 5, 5]

    process(list_a, list_b)