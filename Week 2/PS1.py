count = 0
for char in s:
    if((char.lower() in 'aeiou') == True):
        count +=1

print ('Number of vowels:' + str(count))