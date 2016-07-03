def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if (i in lettersGuessed) == False:
            return False
    return True
