#Rotator 
#Implementing a Caesar Cipher Algorithm

def chr_rotator(ch, n=3):

    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    if ch.lower() not in alphabets:
        return ch
    
    if ch.isupper():
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    index = alphabets.index(ch)
    new_index = (index + n) % len(alphabets)  
    return alphabets[new_index]

text = "AMIT Anand"

print(''.join(list(map(chr_rotator, list(text)))))


