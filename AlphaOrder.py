# Your task is very simple. Just write a function takes an input string of lowercase letters and returns true/false depending
# on whether the string is in alphabetical order or not.

# Examples (input -> output)
# "kata" -> false ('a' comes after 'k')
# "ant" -> true (all characters are in alphabetical order)
# Good luck :)

from string import ascii_lowercase


def alphabetic(s):
    return list(s) == sorted(s)


print(alphabetic('ant'))
