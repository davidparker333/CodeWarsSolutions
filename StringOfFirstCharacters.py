# In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string.

# For example:

str1 = "This Is A Test" # ==> "TIAT"
# Strings will only contain letters and spaces, with exactly 1 space between words, and no leading/trailing spaces.

def make_string(s):
    return ''.join([x[0] for x in s.split()])


print(make_string(str1))
