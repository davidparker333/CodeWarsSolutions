# Write a function that doubles every second integer in a list starting from the left.

# Example:

#   double_every_other([1,2,3,4]) # -> [1, 4, 3, 8]

def double_every_other(lst):
    return [x if i % 2 == 0 else x * 2 for i, x in enumerate(lst)]


print(double_every_other([1, 2, 3, 4]))
