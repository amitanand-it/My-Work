
n = int(input())
for x in range(n):
    try:
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        print(a//b)
    except Exception as e:
        print(f"Error Code: {e}")