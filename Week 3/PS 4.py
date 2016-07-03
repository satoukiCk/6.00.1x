import string
def getAvailableLetters(lettersGuessed):
    a=[]
    import string
    for i in string.ascii_lowercase:
        if (i in lettersGuessed) == False:
            a.append(i)
    return "".join(a)

print getAvailableLetters('')