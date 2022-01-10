# Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout:
# 7 8 9
# 4 5 6
# 1 2 3
#   0

# Cell phone keypad's layout:
# 1 2 3
# 4 5 6
# 7 8 9
#   0

# Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.

# Example:
# "789" -> "123"

# Notes:
# You get a string with numbers only

def computer_to_phone(numbers):
    map = {
        "9": "3",
        "8": "2",
        "7": "1",
        "3": "9",
        "2": "8",
        "1": "7"
    }
    return "".join([map.get(x, x) for x in numbers])


print(computer_to_phone("0789456123"))
