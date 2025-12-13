#Doss, Donivin

#12/13/2025

#Final Project

#Hangman Game

import random

WORDS = ["python", "hangman", "challenge", "development", "computer", "programming", "keyboard"]
word = random.choice(WORDS)
guessed = set()
attempts = 6
done = False

def masked_word(w, g):
    m = ""
    i = 0
    while i < len(w):
        if w[i] in g:
            m += w[i]
        else:
            m += "_"
        i += 1
    return m

while not done:
    print("Word:", " ".join(masked_word(word, guessed)))
    print("Guessed:", " ".join(sorted(guessed)) or "(none)")
    print("Attempts left:", attempts)
    guess = input("Guess a letter: ").lower().strip()
    valid = True
    if len(guess) != 1:
        print("Please enter a single letter.")
        valid = False
    elif not guess.isalpha():
        print("Please enter a letter from a-z.")
        valid = False
    elif guess in guessed:
        print("You already guessed that letter.")
        valid = False
    if valid:
        guessed.add(guess)
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess.")
    current = masked_word(word, guessed)
    if "_" not in current:
        print("You won! The word was", word)
        done = True
    elif attempts <= 0:
        print("You lost! The word was", word)
        done = True