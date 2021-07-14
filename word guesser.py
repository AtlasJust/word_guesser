#word guesser 

import random


name = input("What is your name?")

print("Good Luck !", name)
words = ['rainbow', 'computer', 'here', 'play', 'now', 'pride', 'game', 'book']

word = random.choice(words)

print("Guess The Letters")
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win Congrats")
        print("The Word Is: ", word)
    guess = input("Guess A Letter:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("Im sorry but you have not won this time please try again. and thank you for playing")