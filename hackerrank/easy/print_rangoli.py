"""
#size 3        #size 5
----c----      --------e--------
--c-b-c--      ------e-d-e------
c-b-a-b-c      ----e-d-c-d-e----
--c-b-c--      --e-d-c-b-c-d-e--
----c----      e-d-c-b-a-b-c-d-e
               --e-d-c-b-c-d-e--
               ----e-d-c-d-e----
               ------e-d-e------
               --------e--------


"""


def print_rangoli(size):
    # your code goes here
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    s = alphabets[:size][::-1]
    for i in range(1, 2*size):
        if i <= size:
            print( '--'* (size - i) + '-'.join(list(s[:i])  + list(s[:i-1][::-1])) + '--'* (size-i))
        else:
            j = size - (i - size) 
            print( '--'* (size - j) + '-'.join(list(s[:j] + s[:j-1][::-1])) + '--'* (size-j))





if __name__ == '__main__':
#    n = int(input())
    print_rangoli(10)

