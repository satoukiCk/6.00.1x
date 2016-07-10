def dict_interdiff(d1, d2):
    t1 = ()
    dic1 = {}
    dic2 = {}
    for i in d1.keys():
        for j in d2.keys():
            if i==j:
                dic1[i] = f(d1[i],d2[i])
    for i in d1.keys():
        if not i in d2.keys():
            dic2[i] = d1[i]
    for i in d2.keys():
        if not i in d1.keys():
            dic2[i] = d2[i]
    t = (dic1,dic2)
    return t



