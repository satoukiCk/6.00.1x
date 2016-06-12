a = 'bob'
i = 0
count = 0
while(i <= len(s)-len(a)):
    if(a == s[i:i+3]):
        count +=1
    i+=1
print count