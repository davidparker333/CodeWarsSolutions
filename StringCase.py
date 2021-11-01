# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either 
# lowercase only or uppercase only based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

str1 = "coDe"
str2 = "CODe"
str3 = "coDE"

def solve(s):
    return s.upper() if len([x for x in s if x.isupper()]) > len([x for x in s if x.islower()]) else s.lower()


print(solve(str1))
