# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised
#  of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
arr1 =  [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

arr2 =  [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    arr =  [i % 2 for i in integers]
    return integers[arr.index(1)] if arr.count(0) > 1 else integers[arr.index(0)]

print(find_outlier(arr1))