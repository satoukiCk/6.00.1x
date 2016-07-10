def dotProduct(listA, listB):
    sum = 0
    i = 0
    while i < len(listA):
        sum += listA[i] * listB[i]
        i +=1
    return sum