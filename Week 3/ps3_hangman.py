import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if (i in lettersGuessed) == False:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    a = ''
    for i in secretWord:
        if i in lettersGuessed:
            a += i
        else:
            a += "_"
        count += 1
    return a


def getAvailableLetters(lettersGuessed):
    a = []
    import string
    for i in string.ascii_lowercase:
        if (i in lettersGuessed) == False:
            a.append(i)
    return "".join(a)


def hangman(secretWord):
    guessleft = 8
    print 'Welcome to the game, Hangman!'
    print ("I am thinking of a word that is " +str(len(secretWord)) +  " letters long.")
    lettersGuessed = []
    GuessedWord = getGuessedWord(secretWord,lettersGuessed)
    while guessleft > 0:
        print "------------"
        print ("You have " + str(guessleft) + " guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print ("Available letters: " + availableLetters)
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter:" + GuessedWord)
        else:
            lettersGuessed.append(guess)
            temp = GuessedWord
            GuessedWord = getGuessedWord(secretWord,lettersGuessed)
            if temp == GuessedWord:
                print ("Oops! That letter is not in my word: " + GuessedWord)
                guessleft -= 1
            else:
                print("Good Guess: " + GuessedWord)
                if GuessedWord == secretWord:
                    print "------------"
                    print "Congratulations, you won!"
                    return
    print "------------"
    print "Sorry, you ran out of guesses. The word was else. "




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
