#Write a program to print the number of words in a given sentence

s = "The quick brown fox jumped over the lazy dog"

def print_num_words(s):
    return len(s.split(" "))

print(print_num_words(s))