# Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

import math


def heron(a, b, c):
    return round(math.sqrt((s := (a+b+c)/2) * (s-a) * (s-b) * (s-c)), 2)
