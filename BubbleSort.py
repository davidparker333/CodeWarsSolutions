# Implement a function to sort items in a list

nums = [1,7,5,3,5,8,9,5,2,1,5,7,9,-4,0,4,3,82,63,75,144,86,2]

def bubble_sort(nums):
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                is_sorted = False
    return nums

print(bubble_sort(nums))