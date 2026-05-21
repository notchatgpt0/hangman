import random
# imports the random number selector

inputtedpassword = "0"
while inputtedpassword not in "abcdefghijklmnopqrstuvwxyz":
    inputtedpassword = input("Enter in the password required to start the game: ").lower()
else:
    wrongletters = 0
listofwords = ["tree", "car", "nickel", "hangman", "penny", "apple", "battery", "rocket", "music", "eat", "football", "basketball", "baseball", "soccer", "softball", "tennis", "phone", "computer", "spray"]
# the list of words that the program can choose from
selectedword = random.choice(listofwords)
# chooses a random word and puts gives it to the user for them to guess
length = len(selectedword)
if length > 6:
    wrongguesses = 12
else:
    wrongguesses = 8
# code above sets everything to the default value at the start

print("Your word has " + str(length) + " letters, and you have " + str(wrongguesses) + " guesses.")
print("Begin guessing letters")
# tells the player to start guessing letters

display = ["_"] * length
# the display

while "_" in display and wrongletters < wrongguesses:
    userinput = input("Guess a letter: ").lower()
    if userinput in selectedword:
        for i, letter in enumerate(selectedword):
            if letter == userinput:
                display[i] = userinput

        print("Correct guess! You still have " + str(wrongguesses - wrongletters) + " guesses left!")

    else:
        wrongletters += 1
        print("Incorrect guess! You have " + str(wrongguesses - wrongletters) + " guesses left!")

    print(" ".join(display))
# updates the display to show where the correct letters are if the player guesses it, if the player guesses wrong the amount of guesses they have left decreases

if "_" not in display:
    print("You won!")
    # checks if the player has guessed all of the letters and revealed the word
elif wrongletters >= wrongguesses:
    print("You've run out of guesses! The word was: " + selectedword)
    # if the player has ran out of guesses they will lose and be given the word
