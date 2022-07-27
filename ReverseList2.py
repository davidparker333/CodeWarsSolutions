# Write reverseList function that simply reverses lists.

# In place, no built-ins and no [::-1]
def reverse_list(lst):
    i = 0
    j = len(lst) - 1
    while j > i:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


print(reverse_list([1, 2, 3, 4, 5, 6]))
