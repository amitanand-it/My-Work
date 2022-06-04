import math
ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 + bc**2)
mc = ac/2
theta = math.degrees(math.acos((bc/2)/mc))
degree_sign = u'\N{DEGREE SIGN}'
print(f"{round(theta)}{degree_sign}")


"""
rsz_1438840048-2cf71ed69d-findangle.png  is a right triangle,  at .
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°
"""