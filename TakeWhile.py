# Here's another staple for the functional programmer. You have a sequence of values and some predicate for those values.
# You want to get the longest prefix of elements such that the predicate is true for each element. We'll call this the takeWhile function.
# It accepts two arguments. The first is the sequence of values, and the second is the predicate function.
# The function does not change the value of the original sequence.

# is_even = lambda x: not x % 2
# seq = [2, 4, 6, 8, 1, 2, 5, 4, 3, 2]
# take_while(seq, is_even) # -> [2, 4, 6, 8]
# Your task is to implement the takeWhile function.

def take_while(arr, pred_fun):
    res = []
    for x in arr:
        if pred_fun(x):
            res.append(x)
        else:
            break
    return res


print(take_while([2, 4, 6, 8, 1, 2, 5, 4, 3, 2], lambda x: not x % 2))
