# Given two arrays of integers m and n, test if they contain at least one identical element. Return true if they do; false if not.

# Your code must handle any value within the range of a 32-bit integer, and must be capable of handling either array being empty
# (which is a false result, as there are no duplicated elements).


def duplicate_elements(m, n):
    return bool([x for x in m if x in n])


print(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]))
