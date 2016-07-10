def flatten(aList):
    result = []
    for i in aList:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
