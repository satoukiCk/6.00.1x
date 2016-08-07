def getSublists(L, n):
    cnt = 0
    result = []
    sub = []
    cur = 0
    while cur <= (len(L) - n):
        while cnt < n:
            sub.append(L[cnt+cur])
            cnt += 1
        cur += 1
        cnt = 0
        result.append(sub)
        sub = []
    return result