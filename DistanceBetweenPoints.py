# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x and y attributes (X and Y in C#) attributes.

# Write a function calculating distance between Point a and Point b.

# Tests round answers to 6 decimal places.

from math import sqrt


def distance_between_points(a, b):
    return sqrt((b.x - a.x)**2 + (b.y - a.y)**2)
