#Write a function to extract digits from a given string

s = "Th9is is0 a s4tring w83ith n9mber8s i7n i9t"

def extract_digits(s):
    res = ""
    for char in s:
        if char.isnumeric():
            res = res + char
    return int(res)

print(extract_digits(s))