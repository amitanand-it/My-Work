import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(map(str.capitalize, s.lower().split(' ')))

    

if __name__ == '__main__':
    print(solve('ALLISON            heck'))
    print(solve('ALLISON  heck 123hello'))

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()