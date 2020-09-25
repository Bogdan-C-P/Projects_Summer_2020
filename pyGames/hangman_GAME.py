import random
import string

WORDLIST_FILENAME = "words.txt" #name of the file with all the words in it


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    word = ""
    for leter in secret_word:
        if leter in letters_guessed:
            word += leter
    if word == secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    seq = ["_ "] * len(secret_word)
    i = 0
    for leter in secret_word:
        if leter in letters_guessed:
            seq[i] = leter
        i += 1
    return seq


def get_available_letters(letters_guessed):
    word = "abcdefghijklmnopqrstuvwxyz"
    word2 = ""
    for w in word:
        if w not in letters_guessed:
            word2 += w
    return word2


def hangman(secret_word):

       i=6
       r=3
       letters=[""]
       print("Welcome to the game Hangman!")
       print(f"I am thinking of a word that is {len(secret_word)} letters long")
       print("You have 3 warnings left.")
       while True:
           print("------------")
           print(f"You have {i} guesses left")
           print("Available Letters: ", get_available_letters(letters))
           x=input("Please guess a letter: ").lower()
           if x.isalpha() == False :
               r-=1
               print(f"You have {r} warnings left")
           if x in letters:
               r-=1
               print(f"You have {r} warnings left")
           letters.append(x)
           if x in secret_word:
               print("Good guess: ", end="")
               print("".join(get_guessed_word(secret_word, letters)))
           else:
               print("Oops! That letter is not in my word: ",end="")
               print("".join(get_guessed_word(secret_word, letters)))
               i=i-1
           if is_word_guessed(secret_word, letters) == True or i==0 or r==0:
               break
       if is_word_guessed(secret_word, letters) == True :
           print("Congratulations, you won!")
           print("Your total score for this game is: ", i*len(set(secret_word)))
       else:
           print(f"Sorry, you ran out of guesses. The word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------




if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)