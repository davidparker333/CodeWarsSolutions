# Given a string, swap the case for each of the letters.

# Examples
# ""           -->   ""
# "CodeWars"   -->   "cODEwARS"
# "abc"        -->   "ABC"
# "ABC"        -->   "abc"
# "123235"     -->   "123235"

def swap(s):
    return ''.join([x.upper() if x.islower() else x.lower() for x in s])


print(swap("CodeWars"))
