def dict_invert(d):
    invert = {}
    for i in d.keys():
        if d[i] in invert.keys():
            additem(invert[d[i]],i)
        else:
            invert[d[i]] = []
            additem(invert[d[i]],i)
    return invert

def additem(list,i):
    list.append(i)
    list.sort()
    return list[:]
