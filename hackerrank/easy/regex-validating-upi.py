import re

n = int(input())

for _ in range(n):
    
    uid = input()
    
    if len(uid) != 10 or not re.search(r'[A-Z].*?[A-Z]',uid) or not re.search(r'[0-9].*?[0-9].*?[0-9]', uid) or not re.match(r"[a-zA-Z0-9]", uid) or  re.search(r"(.).*?\1", uid):
        print('Invalid')
    else:
        print('Valid')

"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid
"""