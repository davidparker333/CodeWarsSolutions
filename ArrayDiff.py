# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

arr1a = [1,2]
arr1b = [1]
# == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

arr2a = [1,2,2,2,3]
arr2b = [2]
# == [1,3]

def array_diff(a, b):
    res = []
    for ele in a:
        if ele not in b:
            res.append(ele)
    return res

print(array_diff(arr2a, arr2b))