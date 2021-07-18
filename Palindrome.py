#Write a function to check if a string is palindrome or not

def palindrome(s):
    if s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1]:
        return True
    else:
        return False

print(palindrome("Racecar"))

print(palindrome("Murder for a jar of red rum"))