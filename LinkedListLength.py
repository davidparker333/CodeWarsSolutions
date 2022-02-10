# Implement the method length, which accepts a linked list (head), and returns the length of the list.

# For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.

# The linked list is defined as follows:

from itertools import count


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# Note: the list may be null and can hold any type of value.

# Good luck!


def length(head):
    if head is not None:
        counter = 1
        while head.next:
            head = head.next
            counter += 1
        return counter
    return 0


four = Node(4)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)

print(length(one))
