def minion_game(string):
    # your code goes here
    # The Minion Game in Python - Hacker Rank Solution START
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    else :
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)



"""




def count_overlapping(string, substr):
    count = 0
    for i, ch in enumerate(string):
        if string[i:].startswith(substr):
            count += 1
    return count

d = dict() 

def calculate_score(string, substr):

    score = 0

    for i, x in substr:
        y = ''
        # for z in string[string.index(x, i):]:
        for z in string[i:]:
            y += z
            if y not in d:
                # print(y, count_overlapping(string, y))
                score += count_overlapping(string, y)
                # print(score)
                d[y] = 1

    return(score)

def minion_game(string):

    vowels = 'AEIOU'

    # Withoud Vowels
    # Stuart score
    # print('FOR STUART')
    # a_str = [x for i, x in enumerate(string) if x not in string[:i] and x not in vowels]
    a_str = [(i, x) for i, x in enumerate(string) if x not in vowels]
    a_score = calculate_score(string, a_str)
    # print(a_score)

    # kevin score
    # print('FOR KEVIN')
    # b_str = [x for i, x in enumerate(string) if x not in string[:i] and x in vowels]
    b_str = [(i, x) for i, x in enumerate(string) if x in vowels]
    # print("B STR: ", list(enumerate(b_str)))
    # b_str = list(enumerate(b_str, start=1))
    # print(b_str)
    b_score = calculate_score(string, b_str)
    # print(b_score)

    if a_score > b_score:
        print("Stuart", a_score)
    elif b_score > a_score:
        print("Kevin", b_score)
    else:
        print("Draw")





if __name__ == '__main__':
    s = 'banana' 
    s = 'BAANANAS'
    minion_game(s.upper())

"""
"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.
"""