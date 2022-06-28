# Write a function groupIn10s which takes any number of arguments, groups them into tens, and sorts each group in ascending order.

# The return value should be an array of arrays, so that numbers between 0 and9 inclusive are in position 0, numbers between 10 and 19 are in position 1, etc.

# Here's an example of the required output:

# grouped = group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50)

# grouped[0]     # [3, 8]
# grouped[1]     # [12, 17, 19]
# grouped[2]     # [25]
# grouped[3]     # [35, 38]
# grouped[4]     # None
# grouped[5]     # [50]

from math import ceil


def trim(arr):
    if arr[-1] == None:
        arr = arr[:-1]
    return arr


def group_in_10s(*args):
    if not args:
        return []
    max = ceil(sorted(args)[-1] / 10)
    res = []
    for i in range(max+1):
        group = sorted([x for x in args if x >= i * 10 and x < (i+1) * 10])
        res.append(group if group else None)
    return trim(res)


print(group_in_10s(12, 10, 11, 13, 25, 28, 29, 49, 51, 90))
