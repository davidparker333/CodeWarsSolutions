# Write an echoProgram function (or echo_program depend on language) that returns your solution source code as a string.

def echo_program():
    return open(__file__).read()


print(echo_program())
