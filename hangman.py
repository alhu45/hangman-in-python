import random
from words import wordsHangman 
import string

def hangman():
    lives = 6
    #gets random word from the list of words
    word = random.choice(wordsHangman).upper()
    wordLetters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #all the letters in the alphabet
    usedLetters = set()
    #print(word)

    print(f"Welcome to Hangman! You currently have {lives} lives.") 

    for letters in wordLetters:
        wordUnsolved = print("_", end=" ")

    while len(wordLetters) > 0 and lives > 0:
        guess = input("\nGuess a letter: ").upper()
        #checks if the guess is a valid letter in the alphabet

        if guess in alphabet - usedLetters:
            usedLetters.add(guess)
            print(f"Letters used: {' '.join(usedLetters)}")
            #checks if the guess is in the word
            if guess in wordLetters:
                wordLetters.remove(guess)
                print(f"Correct! {guess} is in the word.")
            else:
                lives -= 1
                print(f"Sorry, {guess} is not in the word. You have {lives} lives left.")
        #checks if the guess was already used or not a valid letter
        elif guess in usedLetters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Please try again.")

        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ', ' '.join(wordList))
        
    if lives == 0:
        print(f"Sorry, you lost. The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word} correctly!")

    
hangman()

        