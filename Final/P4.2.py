def longestRun(L):
    for n in range(len(L),1,-1):
        sublists = getSublists(L,n)
        if IsSorted(sublists):
            return n
    return 1
def IsSorted(L):
    unsorted = 0
    for sublist in L:
        for i in range(len(sublist)-1):
            if sublist[i] > sublist[i+1]:
                unsorted += 1
                break
    return unsorted != len(L)
