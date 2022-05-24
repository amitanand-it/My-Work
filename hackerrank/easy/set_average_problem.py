def average(array):
    # your code goes here
    data = set(array)
    return sum(data)/len(data)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)