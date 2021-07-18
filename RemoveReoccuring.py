#Given a string as your inputs, delete any recorruring character

s = "This is a sentence with some reoccuring characters in it"

def delete_reoccuring(s):
    res_string = ""
    char_dict = {}
    for char in s:
        if char not in char_dict.keys():
            char_dict[char] = 1
            res_string = res_string + char
        else:
            continue
    return res_string

print(delete_reoccuring(s))