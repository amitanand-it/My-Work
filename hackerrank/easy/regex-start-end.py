import re
s1 = input()
s2 = input()

import re
window_frame = len(s2) 

match_flag=False
for i  in range(len(s1)):
    if s1[i:window_frame+i] == s2: 
        print((i, i + window_frame -1))
        match_flag = True
if match_flag == False:
    print((-1, -1))

"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
Task
You are given a string .
Your task is to find the indices of the start and end of string  in .

Input Format

The first line contains the string .
The second line contains the string .

Constraints



Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)
"""