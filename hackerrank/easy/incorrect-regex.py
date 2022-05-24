import re

for _ in range(int(input())):
    pattern = input()
    try:
        re.compile(pattern)
    except Exception as e:
        print(False)
    else:
        print(True)