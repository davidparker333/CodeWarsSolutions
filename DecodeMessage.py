# You have managed to intercept an important message and you are trying to read it.

# You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

# You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

# For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

# You read the first sentence:

message = "r slkv mlylwb wvxlwvh gsrh nvhhztv"
# After a few minutes you manage to decode it:

# "i hope nobody decodes this message"
# Create a function that will instantly decode any of these messages

# You can assume no punctuation or capitals, only lower case letters, but remember spaces!


def decode(message):
    alpha_dict = {
        32: 32
    }
    lower = [x for x in range(97, 123)]
    lower_reverse = lower[::-1]
    for i, char in enumerate(lower):
        alpha_dict[char] = lower_reverse[i]
    return "".join([chr(alpha_dict.get(ord(x))) for x in message])


print(decode(message))
