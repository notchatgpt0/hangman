import random
# imports the random number selector
import datetime
# imports date

print("Today's date is: " + str(datetime.date.today()))
# prints the current date for the player

def guess(user_input, selected_word, display):
    # checks if the guessed letter is in the word and updates the display
    if user_input in selected_word:
        for i, letter in enumerate(selected_word):
            if letter == user_input:
                display[i] = user_input
        return True
    else:
        return False




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
wrong_letter_list = []
# stores all the wrong letters the player guessed
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
    if len(user_input) != 1 or user_input == "":
        print("Please enter a single letter only. Try again.")
        continue
    if guess(user_input, selected_word, display):
        print("Correct guess! You still have " + str(guesses - wrong_letters) + " guesses left!")
        correct_letters += selected_word.count(user_input)
    else:
        wrong_letters += 1
        wrong_letter_list.append(user_input)
        # appends wrong letters into the list
        print("Incorrect guess! You have " + str(guesses - wrong_letters) + " guesses left!")
    print(" ".join(display))
# updates the display to show where the correct letters are if the player guesses it, if the player guesses wrong the amount of guesses they have left decreases
if "_" not in display:
    print("You won!")
    # checks if the player has guessed all of the letters and revealed the word
elif wrong_letters >= guesses:
    print("You've run out of guesses! The word was: " + selected_word)
    # if the player has ran out of guesses they will lose and be given the word

print("Statistics:")

if correct_letters > 0:
    guess_ratio = round(float(guesses / correct_letters), 2)
    # default difficulty ratio value, difficult ratio is based on guesses divided by correct letters
    print(f"\tYou guessed {guess_ratio} time(s) for each correct guess.")
    # prints the guess ratio

print("\tWrong letters guessed: " + str(wrong_letter_list))
