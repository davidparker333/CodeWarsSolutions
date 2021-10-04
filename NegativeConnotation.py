# You will be given a string with sets of characters, (i.e. words), seperated by between one and three spaces (inclusive).

# Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), you need to determine whether it falls
#  into the positive/first half of the alphabet ("a"-"m") or the negative/second half ("n"-"z").

# Return True/true if there are more (or equal) positive words than negative words, False/false otherwise.

string1 = "A big brown    fox caught a bad rabbit" # => True/true
string2 = "Xylophones can obtain Xenon." # => False/false

def connotation(strng):
    positive_count = 0
    negative_count = 0
    list_of_words = strng.split()
    for word in list_of_words:
        word = word.lower()
        if ord(word[0]) >= 97 and ord(word[0]) <= 109:
            positive_count += 1
        else:
            negative_count += 1
    return positive_count >= negative_count
    

print(connotation(string2))