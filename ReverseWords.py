# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    space = ' ' if ' '.join(text.split()) == text else '  '
    return space.join([x[::-1] for x in text.split()])


print(reverse_words('This is an example!'))
