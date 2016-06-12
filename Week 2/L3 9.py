print "Please think of a number between 0 and 100!"
low = 0
high = 100
while(low != high):
    cur = ( low + high ) / 2
    print ("Is your secret number " + str(cur) + "?")
    i = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if i == 'h':
        high = cur
    elif i == 'l':
        low = cur
    elif i == 'c':
        break
    else:
        print "Sorry, I did not understand your input."
print ("Game over. Your secret number was: " + str(cur))