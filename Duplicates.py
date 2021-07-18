#Write a function that prints any item in a list that is a duplicate

lis = [1,1,2,3,4,4,5,6,7,8,8]

def find_dupes(lis):
    return set([x for x in lis if lis.count(x) > 1])

print(find_dupes(lis))