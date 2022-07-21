# y grandfather's memory we will write a function using his formula!

# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.
# Example
# predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
# Note: the result should be rounded down to the nearest integer.

def predict_age(*ages):
    return int((sum([x**2 for x in ages]) ** .5) // 2)


print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
