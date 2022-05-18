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
    letters = alphabets[:size]
    print(letters)




if __name__ == '__main__':
#    n = int(input())
    print_rangoli(3)

