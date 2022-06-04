from datetime import datetime, timedelta

for _ in range(int(input())):
    dt1 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    dt2 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    print(int(abs((dt1 - dt2).total_seconds())))

"""

months = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
months = { month: i for i, month in enumerate(months, start=1) }
# print(months)
from datetime import datetime, timedelta

output = []
# for _ in range(int(input())):
for _ in range(1):
    # t1 = input().split()
    # t2 = input().split()
    sum = 0
    t1 = 'Fri 11 Feb 2078 00:05:21 +0400'
    _, dd, mon, yyyy, t1, tz1 = t1.split()
    mon = months[mon]

    dt1  = datetime(int(yyyy), int(mon), int(dd))


    hh, mm, ss = map(int, t1.split(':'))

    print(dd, mon, yyyy, t1, tz1, hh, mm, ss)

    if tz1.startswith('+'):
        sec = (hh*3600 + mm*60 + ss) - (int(tz1[1:3])*3600 + int(tz1[3:5])*60) 
    else:
        sec = (hh*3600 + mm*60 + ss) + (int(tz1[1:3])*3600 + int(tz1[3:5])*60) 

    sum  += sec 

    t2 = 'Mon 29 Dec 2064 03:33:48 -1100'

    _, dd, mon, yyyy, t1, tz1 = t2.split()
    mon = months[mon]


    dt2  = datetime(int(yyyy), int(mon), int(dd))

    hh, mm, ss = map(int, t1.split(':'))

    print(dd, mon, yyyy, t1, tz1, hh, mm, ss)

    # if tz1.startswith('+'):
    #     sec = (hh*3600 + mm*60 + ss) - (int(tz1[1:3])*3600 + int(tz1[3:5])*60) 
    # else:
    #     sec = (hh*3600 + mm*60 + ss) + (int(tz1[1:3])*3600 + int(tz1[3:5])*60) 

    sum  += sec 


    # 414041493
    # correct : 413962293

    res = (dt1 - dt2).total_seconds() + sum
    

    output.append(abs(int(res))) 
    # print(abs(int(res)))

for x in output:
    print(x)
        

"""


"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .

Constraints

Input contains only valid timestamps
.
Output Format

Print the absolute difference  in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200
Explanation 0

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  seconds or  seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 
"""