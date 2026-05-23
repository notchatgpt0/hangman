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

def show_stats(guesses, correct_letters, letter_list):
    # displays the statistics at the end of the game
    print("Statistics:")
    if correct_letters > 0:
        guess_ratio = round(float(guesses / correct_letters), 2)
        print(f"\tYou guessed {guess_ratio} time(s) for each correct guess.")
    print("\tUsed letters: " + str(letter_list))

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
letter_list = []
# stores all the letters the player has guessed
unused_letters = list("abcdefghijklmnopqrstuvwxyz")
# this list is used to prevent a player from guessing the same letter again

list_of_words = ["tree", "car", "nickel", "hangman", "penny", "apple", "battery", "rocket", "music", "eat", "football", "basketball", "baseball", "soccer", "softball", "tennis", "phone", "computer", "spray"]
list_of_hints = ["nature", "vehicle", "coin", "game", "coin", "fruit", "electronics", "space", "entertainment", "action", "sport", "sport", "sport", "sport", "sport", "sport", "technology", "technology", "action"]
# parallel lists — same index refers to the same word and its hint

selected_index = random.randint(0, len(list_of_words) - 1)
selected_word = list_of_words[selected_index]
selected_hint = list_of_hints[selected_index]
# chooses a random word and its matching hint using the same index

correct_letters = 0
# counts how many correct letters were guessed

length = len(selected_word)
if length > 6:
    guesses = 10
else:
    guesses = 8
# code above sets everything to the default value at the start

print("Hint: This word is related to " + selected_hint)
# prints the hint
print("Your word has " + str(length) + " letters, and you have " + str(guesses) + " guesses.")
# prints word statistics
print("Begin guessing letters")
# tells the player to start guessing letters

display = ["_"] * length
# the display
print(" ".join(display))
# pre prints so that the player knows how many letters are in the hidden word

while "_" in display and wrong_letters < guesses:
    user_input = input("Guess a letter: ").lower()
    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a single letter only. Try again.")
        continue
        # only allows single letter inputs
    if user_input not in unused_letters:
        print("You already guessed " + user_input + "! Try a different letter.")
        continue
        # prevents players from guessing the same letters multiple times
    unused_letters.remove(user_input)
    # removes used letters from the list
    letter_list.append(user_input)
    # adds used letters into a new list
    if guess(user_input, selected_word, display):
        print("Correct guess! You still have " + str(guesses - wrong_letters) + " guesses left!")
        correct_letters += selected_word.count(user_input)
    else:
        wrong_letters += 1
        print("Incorrect guess! You have " + str(guesses - wrong_letters) + " guesses left!")
    print("Used letters: " + ", ".join(letter_list))
    # prints used letters
    print(" ".join(display))
# updates the display to show where the correct letters are if the player guesses it, if the player guesses wrong the amount of guesses they have left decreases

if "_" not in display:
    print("You won!")
    # checks if the player has guessed all of the letters and revealed the word
elif wrong_letters >= guesses:
    print("You've run out of guesses! The word was: " + selected_word)
    # if the player has ran out of guesses they will lose and be given the word

show_stats(guesses, correct_letters, letter_list)
