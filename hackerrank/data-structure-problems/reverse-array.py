
a = [2,3,1,4,5,1,1]
print(a[::-1])

# Swapping index values where sum = length of array
for i in range(len(a)//2):
    a[i], a[len(a)-1 -i] = a[len(a)-1-i], a[i]

print(a)

