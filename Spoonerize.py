# A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with amusing results.

# In its most basic form a spoonerism is a two word phrase in which only the first letters of each word are swapped:

str1 = "not picking"  # --> "pot nicking"

# Your task is to create a function that takes a string of two words, separated by a space: words and returns a spoonerism of those words in a string, as in the above example.


def spoonerize(words):
    return " ".join([f'{words.split()[i-1][0]}{w[1:]}' for i, w in enumerate(words.split())])


print(spoonerize(str1))
