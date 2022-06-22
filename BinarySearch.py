# Implement a function that finds a given value in a given list and return the index or -1 if not present

def search(arr, target, l=None, r=None):
    # For ease of calling func, set initial l and r
    if l == None and r == None:
        l, r = 0, len(arr)

    # The target is not found
    if r < l or target > arr[-1]:
        return -1

    # Get the midpoint index
    mid = (r + l) // 2

    # Check if we've found the target
    if arr[mid] == target:
        return mid

    # The target is on the right
    if target > arr[mid]:
        l = mid + 1
    # The target is on the left
    else:
        r = mid - 1

    # Recurse with the new pointer positions
    return search(arr, target, l, r)


l = [1, 3, 4, 6, 8, 9, 12, 15, 18, 22, 33, 56, 78, 79, 90]
print(search(l, 8))
