m = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16], 
] 

# print(list(zip(*m)))
r = c = 4
j = c//2  
print(j)
for col in range(j, c):
    for row in range(r):
        print(m[row][col], end=" ")
    print()


