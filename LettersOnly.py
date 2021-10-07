# Let's assume we need "clean" strings. Clean means a string should only contain letters a-z, A-Z and spaces. We assume that there are no double spaces or line breaks.

# Write a function that takes a string and returns a string without the unnecessary characters.

# Examples
# remove_chars('.tree1')    ==> 'tree'

# remove_chars("that's a pie$ce o_f p#ie!")  ==> 'thats a piece of pie'

# remove_chars('john.dope@dopington.com')    ==> 'johndopedopingtoncom'

# remove_chars('my_list = ["a","b","c"]')    ==> 'mylist  abc'

# remove_chars('1 + 1 = 2')    ==> '    ' (string with 4 spaces)

# remove_chars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_")  ==> '' (empty string)

str1 = "that's a pie$ce o_f p#ie!"

str2 = 'john.dope@dopington.com'

str3 = 'my_list = ["a","b","c"]'

str4 = '1 + 1 = 2'

str5 = "0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_"

def remove_chars(s):
    return "".join([char for char in s if char.isalpha() or char == " "])

print(remove_chars(str5))