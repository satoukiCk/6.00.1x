def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) <= 1:
        return True
    return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])
