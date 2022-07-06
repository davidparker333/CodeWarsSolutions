# You will be given 2 lists of tuples from a time series. The first value represents seconds,
# and the second value is a measurement. Sum the measurement values from each series
# at each time interval. If a time interval is present in one series and not the other,
# ignore it. Return a list of tuples

a = [(1, 1.2), (2, 1.7), (3, 2.3)]
b = [(2, 1), (3, 3.3), (4, 4.6)]


def sum_series(a, b):
    '''
    2 pointers - efficient solution
    Time - O(n) - linear
    Space - O(1) - constant
    '''
    i = 0
    j = 0
    res = []
    while i < len(a) and j < len(b):
        ele_a = a[i]
        ele_b = b[j]
        if ele_a[0] == ele_b[0]:
            res.append((ele_a[0], ele_a[1] + ele_b[1]))
            i += 1
            j += 1
        elif ele_a[0] > ele_b[0]:
            j += 1
        elif ele_a[0] < ele_b[0]:
            i += 1
    return res


def sum_series_2(a, b):
    '''
    Horrible, but one-liner
    '''
    return [(x, y + list(filter(lambda z: z[0] == x, b))[0][1]) for x, y in a if x in [n for n, m in b]]


print(sum_series(a, b))
