def isPalindrome(aString):
    if len(aString) < 1:
        return True
    else:
        return aString[0] == aString[-1] and isPalindrome(aString[1:-1])