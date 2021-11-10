# Write a function that removes every lone 9 that is inbetween 7s.

# seven_ate9('79712312') => '7712312'
# seven_ate9('79797') => '777'
# Input: String Output: String

str1 = '79712312'
str2 = '79797'


def seven_ate9(str_):
    while '797' in str_:
        str_ = str_.replace('797', '77')
    return str_


print(seven_ate9(str1))
