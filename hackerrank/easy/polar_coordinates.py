import math
c = complex(input())
r = math.sqrt(c.real**2 + c.imag**2) 
phi = math.atan2(c.imag,c.real)

print(r)
print(phi)