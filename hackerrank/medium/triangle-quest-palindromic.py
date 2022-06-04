"""
print below triangle
1
121
12321
1234321
123454321
"""
print("\nTriangle 1")

for i in range(1,6):

    # Method 1 
    # print(''.join(map(str,list(range(1,x+1)) + list(range(x-1,0, -1)))))

    # Method 2 
    # print(''.join([f"{x}" for x in  list(range(1,x+1)) + list(range(x-1,0, -1)) ]))

    # Method 3 
    #print('123456789'[:i]  + '123456789'[:i-1][::-1])

    # Method 4 using power method as this is series of square like pow(1,2) + power(11,2) + ...
    print (((10**i - 1)//9)**2)


# NOW PRINT BELOW TRIANGLE

"""
1
22
333
4444
55555
"""
print("\nTriangle 2")
for i in range(1,6):
    print (((10**i - 1)//9)*i)
