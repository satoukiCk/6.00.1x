def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    mid = len(aStr)/2
    if char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char , aStr[:mid])
    else:
        return isIn(char , aStr[mid+1:])
