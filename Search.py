# Given an array of n unsorted elements, write a function to search a given element x in array. Return its index. If it occurs more than once, return all indexes

arr = [1,8,4,2,7,9,4,2,7,9,3]

def search(arr, target):
    res = []
    for i in range(len(arr)):
        if arr[i] == target:
            res.append(i)
    if res == []:
        return "Not present in list"
    return res

print(search(arr, 7))