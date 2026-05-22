import random
# imports the random number selector
 
inputted_password = input("Enter in the password required to start the game: ")
# ask for the alphanumeric input
 
has_letter = inputted_password.isalpha()
has_digit = inputted_password.isdigit()
has_symbol = False
for character in inputted_password:
    if character not in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
        has_symbol = True
# variables to check if the inputted password by the user will have a letter and a digit later
 
while has_letter or has_digit or has_symbol:
    print("Password must have at least one letter and one number. Try again.")
    inputted_password = input("Enter in the password required to start the game: ")
    has_symbol = False
    for character in inputted_password:
        if character not in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            has_symbol = True
    has_letter = inputted_password.isalpha()
    has_digit = inputted_password.isdigit()
# checks to see if the inputted password has a letter and digit
    
wrong_letters = 0
list_of_words = ["tree", "car", "nickel", "hangman", "penny", "apple", "battery", "rocket", "music", "eat", "football", "basketball", "baseball", "soccer", "softball", "tennis", "phone", "computer", "spray"]
# the list of words that the program can choose from
 
selected_word = random.choice(list_of_words)
# chooses a random word and puts gives it to the user for them to guess
 
correct_letters = 0
# counts how many correct letters were guessed
 
length = len(selected_word)
if length > 6:
    guesses = 12
else:
    guesses = 8
# code above sets everything to the default value at the start
 
print("Your word has " + str(length) + " letters, and you have " + str(guesses) + " guesses.")
print("Begin guessing letters")
# tells the player to start guessing letters
 
display = ["_"] * length
# the display
 
print(" ".join(display))
# pre prints so that the player knows how many letters are in the hidden word
 
while "_" in display and wrong_letters < guesses:
    user_input = input("Guess a letter: ").lower()
    if user_input in selected_word:
        for i, letter in enumerate(selected_word):
            if letter == user_input:
                display[i] = user_input
        print("Correct guess! You still have " + str(guesses - wrong_letters) + " guesses left!")
        correct_letters += selected_word.count(user_input)  # counts duplicate letters too
    else:
        wrong_letters += 1
        print("Incorrect guess! You have " + str(guesses - wrong_letters) + " guesses left!")
    print(" ".join(display))
# updates the display to show where the correct letters are if the player guesses it, if the player guesses wrong the amount of guesses they have left decreases
 
if "_" not in display:
    print("You won!")
    # checks if the player has guessed all of the letters and revealed the word
elif wrong_letters >= guesses:
    print("You've run out of guesses! The word was: " + selected_word)
    # if the player has ran out of guesses they will lose and be given the word
 
if correct_letters > 0:
    guess_ratio = round(float(guesses / correct_letters), 2)
    # default difficulty ratio value, difficult ratio is based on guesses divided by correct letters
    print("Your score is " + str(guess_ratio) + " guesses per correct guess.")
    # prints the guess ratio
