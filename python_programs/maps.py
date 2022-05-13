"""
MAP and LAMBDA
map(function, iterable[, iterable1, iterable2,..., iterableN])
"""

#double all numbers using map 
def double_num(n: int=0): 
    return n*2
#print(list(map(double_num, [2, 8, 89])))

#double all numbers using lambda and map 
#print(list(map(lambda x: x+x, [2, 8, 89])))

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print("IN: ", numbers1)
print("IN: ", numbers2)
print("OUT: ",list(result))


# map() can listify the list of strings individually
# List of strings
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print("IN:  ", l)
print("OUT: ", test)

#Getting the length of each word and convert to dict tuple 
words = ["Welcome", "to", "Real", "Python"]
wl = list(map(len,  words))
print(tuple(zip(words, wl)))
print(dict(zip(words, wl)))


#Map and string function
string_it = ["processing", "strings", "with", "map "]
print(list(map(str.capitalize, string_it)))
print(list(map(str.upper, string_it)))
print(list(map(str.lower, string_it)))

#processing strings and remove dots using map
with_dots = ["processing..", "...strings", "with....", "..map.."]
print(list(map(lambda x: x.strip('.'), with_dots)))

#Removing Punctuation
import re
from xml.sax.handler import all_properties

def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)

text = """Some people, when confronted with a problem, think
... "I know, I'll use regular expressions."
... Now they have two problems. Jamie Zawinski"""

print(text)
print(' '.join((map(remove_punctuation, text.split()))))

