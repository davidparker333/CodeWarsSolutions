# Task
# Given an array of numbers and an index, return the index of the least number larger than the element at the given index,
# or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

# Notes
# Multiple correct answers may be possible. In this case, return any one of them.
# The given index will be inside the given array.
# The given array will, therefore, never be empty.

# Example
# least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
# least_larger( [4, 1, 3, 5, 6], 4 )  -> -1

def least_larger(a, i):
    m = min([x for x in a if x > a[i]], default=[])
    if m != []:
        return a.index(m)
    return -1


print(least_larger([-2, -1, -8, -1, -3, 1, 0, -8, -1, 5, -5, -5], 3))
