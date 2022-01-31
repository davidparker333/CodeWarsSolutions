# Write a function that accepts two arguments: an array/list of integers and another integer (n).

# Determine the number of times where two integers in the array have a difference of n.

# For example:

# [1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
# [1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)

from itertools import combinations


def int_diff(arr, n):
    return sum(1 for x, y in combinations(arr, 2) if abs(x - y) == n)


print(int_diff([1, 1, 5, 6, 9, 16, 27], 4))
