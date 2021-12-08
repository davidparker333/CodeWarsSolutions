# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

# Examples
num1 = -123  # ->  321
# -456 -> -654
# 1000 ->    1


def reverse_number(n):
    return int(str(n)[::-1]) if '-' not in str(n) else int('-' + str(n)[::-1].replace('-', ''))


print(reverse_number(num1))
