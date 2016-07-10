def satisfiesF(L):
    L1 = []
    for i in L:
        if f(i):
            L1.append(i)

    L[:] = L1
    return len(L)


def f(s):
    return 'a' in s or 'b' in s


L = ['a','b','b','c','a','b']
print satisfiesF(L)
print L