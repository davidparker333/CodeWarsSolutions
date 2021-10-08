# A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

# That being said, complete the function which receives a word and returns true if it's a comfortable word and false otherwise.

# The word will always be a string consisting of only ascii letters from a to z.



# To avoid problems with image availability, here's the lists of letters for each hand:

# Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
# Right: y, u, i, o, p, h, j, k, l, n, m
# Examples
str1 = "yams" # -->  true
str2 = "test" # -->  false

def comfortable_word(word):
    letters = [['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'],\
        ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']]
    current_hand = ''
    for l in word:
        if l in letters[0]:
            if current_hand == 'left':
                return False
            elif current_hand == 'right':
                current_hand = 'left'
                continue
            elif current_hand == '':
                current_hand = 'left'
        elif l in letters[1]:
            if current_hand == 'right':
                return False
            elif current_hand == 'left':
                current_hand = 'right'
                continue
            elif current_hand == '':
                current_hand = 'right'
    return True

print(comfortable_word(str2))