# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

# --> "alpha beta gamma delta alpha beta gamma delta"


def remove_consecutive_duplicates(s):
    res = []
    for x in s.split():
        if x != (res or [None])[-1]:
            res.append(x)
    return " ".join(res)


print(remove_consecutive_duplicates(
    "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
