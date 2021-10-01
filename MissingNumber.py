# The following was a question that I received during a technical interview for an entry level software developer position.
# I thought I'd post it here so that everyone could give it a go:

# You are given an unsorted array containing all the integers from 0 to 100 inclusively. However, one number is missing.
# Write a function to find and return this number. What are the time and space complexities of your solution?

nums = [i for i in range(1,101) if i != 66]

def find_missing_nums(nums):
    should_be = sum(range(1,101))
    actually_is = sum(nums)
    return should_be - actually_is

print(find_missing_nums(nums))