def biggest(aDict):
    maxnum = -1
    for key in aDict.keys():
        if len(aDict[key]) > maxnum:
            cur = key
            maxnum = len(aDict[key])
    if maxnum == -1:
        return None
    else:
        return cur