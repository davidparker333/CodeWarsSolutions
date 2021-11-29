# For this kata you will have to forget how to add two numbers.

# It can be best explained using the following meme:

# Dayane Rivas adding up a sum while competing in the Guatemalan television show "Combate" in May 2016

# In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)

# You may assume both integers are positive integers.

def add(num1, num2):
    num1, num2 = str(num1), str(num2)
    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1))
    elif len(num2) > len(num1):
        num1 = num1.zfill(len(num2))
    res = zip([int(x) for x in list(str(num1))], [int(x)
              for x in list(str(num2))])
    return int("".join([str(sum(r)) for r in res]))


print(add(2, 11))
