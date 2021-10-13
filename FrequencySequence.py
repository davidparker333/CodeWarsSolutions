# Return an output string that translates an input string s/$s by replacing each character in s/$s with a number representing the number of times that character
#  occurs in s/$s and separating each number with the character(s) sep/$sep.

# freq_seq("hello world", "-"); // => "1-1-3-3-2-1-1-2-1-3-1"
# freq_seq("19999999", ":"); // => "1:7:7:7:7:7:7:7"
# freq_seq("^^^**$", "x"); // => "3x3x3x2x2x1"

str1 = "hello world"
str2 = "19999999"
str3 = "^^^**$"

sep1 = "-"
sep2 = ":"
sep3 = "x"

def freq_seq(s, sep):
    return sep.join([str(s.count(i)) for i in s])

print(freq_seq(str3, sep3))
