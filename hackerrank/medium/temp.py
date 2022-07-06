
s = 'amit anand'

print(s.index('a'))
print(s.index('a',2))
print(s.index('a',3))
print(s.index('a',4))

print(s.find('a'))
print(s.find('a',2))
print(s.find('a',3))
print(s.find('a',4))
# return -1 if string not found
print(s.find('a',40))  
print(list(enumerate(s)))

print(*map(lambda x: (x**2, x**3) , range(5)))

from fractions import Fraction
print(Fraction(10, 3))


months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
    'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
months = { month: i for i, month in enumerate(months, start=1) }
# print(months)
from datetime import datetime, timedelta


for _ in range(int(input())):
    t1 = input().split()
    t2 = input().split()
    dt1  = datetime(int(t1[3]), int(months[t1[2]]), int(t1[1]), *list(map(int,t1[4].split(':'))))
    dt2  = datetime(int(t2[3]), int(months[t2[2]]), int(t2[1]), *list(map(int,t2[4].split(':'))))

    res = (dt1 - dt2).total_seconds()


    if t1[5].startswith('+'):
        h, m = int(t1[5][1:3]), int(t1[5][3:])
        res  = res - h * 3600 - m * 60
    else:
        h, m = int(t1[5][1:3]), int(t1[5][3:])
        res  = res + h * 3600 + m * 60

    if t2[5].startswith('+'):
        h, m = int(t2[5][1:3]), int(t2[5][3:])
        res  = res - h * 3600 - m * 60
    else:
        h, m = int(t2[5][1:3]), int(t2[5][3:])
        res  = res + h * 3600 + m * 60


    print(abs(int(res)))


