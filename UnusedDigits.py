# Given a varying number of integer arguments, return the digits that are not present in any of them.

# Example:

# [12, 34, 56, 78]  =>  "09"
# [2015, 8, 26]     =>  "3479"
# Note: the digits in the resulting string should be sorted.

def unused_digits(numbers):
    possible = '0123456789'
    return ''.join(sorted([x for x in possible if x not in str(numbers)]))


print(unused_digits([2015, 8, 26]))
