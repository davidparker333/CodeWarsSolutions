# In this kata, we want to sort the vowels in a special format.

# Task
# Write a function which takes a input string s and return a string in the following way:

   
#                   C|                          R|
#                   |O                          n|
#                   D|                          d|
#    "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
#                   W|                          T|
#                   |A                          |e
#                   R|                          5|
#                   S|                          T|

# Notes:

# List all the Vowels on the right side of |
# List every character except Vowels on the left side of |
# Return every character in its original case
# Each line is seperated with \n
# Invalid input ( undefined / null / integer ) should return an empty string

def sort_vowels(s):
    if not s or isinstance(s, int):
        return ''
    res = ''
    for char in s:
        if char.lower() in 'aeiou':
            res += f'|{char}\n'
        else:
            res += f'{char}|\n'
    return res[:-1]

print(sort_vowels('Codewars'))