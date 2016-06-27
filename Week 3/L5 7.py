def lenRecur(aStr):
    if aStr == '':
        return 0
    else :
        return lenRecur(aStr[1:])+1