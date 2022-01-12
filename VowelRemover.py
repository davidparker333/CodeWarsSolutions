# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"

# y is not considered a vowel for this kata

def shortcut(s):
    return "".join([x for x in s if x not in 'aeiou'])


print(shortcut('goodbye'))
