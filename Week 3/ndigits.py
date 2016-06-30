def ndigits(x):
    x = abs(x)
    if x == 0:
        return 0
    else:
        return 1 + ndigits(x/10)
