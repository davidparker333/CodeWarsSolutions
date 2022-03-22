# Given a mathematical equation that has *,+,-,/, reverse it as follows:

# solve("100*b/y") = "y/b*100"
# solve("a+b-c/d*30") = "30*d/c-b+a"
# More examples in test cases.

# Good luck!

import re


def solve(eq):
    ops = re.findall('[\+\-\/\*]', eq)[::-1]
    vars = re.split('[\+\-\/\*]', eq)[::-1]
    return ''.join([x + ops[i] if i < len(ops) else x for i, x in enumerate(vars)])


print(solve('a+b-c/d*30'))
