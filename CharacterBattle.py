# Groups of characters decided to make a battle. Help them to figure out what group is more powerful. Create a function that will accept 2 variables and
# return the one who's stronger.

# Rules
# Each character has its own power:
#   A = 1, B = 2, ... Y = 25, Z = 26
#   a = 0.5, b = 1, ... y = 12.5, z = 13
# Only alphabetical characters can and will participate in a battle.
# Only two groups to a fight.
# Group whose total power (a + B + c + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples
# "One", "Two"  -->  "Two"
# "ONE", "NEO"  -->  "Tie!"

import string


def battle(x: str, y: str) -> str:
    map = make_map(1)
    map.update(make_map(.5, True))

    left = 0
    right = 0

    for str in x:
        left += map[str]
    for str in y:
        right += map[str]

    if left == right:
        return 'Tie!'
    elif right > left:
        return f'{y}!'
    return f'{x}!'


def make_map(inc, lower=False):
    num = inc
    res = {}
    if lower:
        arr = list(string.ascii_lowercase)
    else:
        arr = list(string.ascii_uppercase)
    for x in arr:
        res[x] = num
        num += inc
    return res


print(battle("One", "Two"))
