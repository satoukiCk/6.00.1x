def nfruits(quantities,pattern):
    for i in pattern[:-1]:
        quantities[i] -= 1
        for k in quantities.keys():
            if k != i:
                quantities[k] +=1
    quantities[pattern[-1]] -= 1
    return max(quantities.values())

print nfruits({'A': 9, 'H': 7, 'L': 5, 'O': 9, 'R': 6, 'Z': 5}, 'RZRRZ')