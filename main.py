
# This is a Guessing Game where the player has to Guess a secret word.

import time
import random




# The universal set of words
repo = ['cat',
        'dog',
        'bunny',
        'book',
        'programming',
        'procastination']





# This Function is used to choose a random word from the universal set
# This word will be our secret word
def choose_word() :
    pos = random.randint(0,len(repo)-1)
    return repo[pos]





# Function to ask the Player the Number of Attempts he wants to have
def Ask_Attempts() :
    while True :
        Attempts = int(input("Enter the maximum number of Attempts : (15-30) "))
        if Attempts > 30 or Attempts < 15 :
            print("Oops , Try Again...")
        else :
            return Attempts





# Function to display the Progress-O-Meter
def disp_progress() :
    for i in range(0 , len(Guess_Word)) :
        if progress[i] :
            print(Guess_Word[i] , end = "")
        else :
            print("." , end = "")

    print()





# Function to ask the Player for the Guess Letter
def make_guess() :
    Guess_Letter = input("Enter a Letter in Lower Case : ")
    if len(Guess_Letter) == 1 and Guess_Letter.isalpha() and Guess_Letter.islower() :
        return Guess_Letter
    else :
        print("Oops , Try Again..")
        return make_guess()




# Function to Update the Progress of the Player
def update_progress(Guess_Letter) :
    for i in range(0,len(Guess_Word)) :
        if not(progress[i]) and Guess_Word[i] == Guess_Letter :
            progress[i] = True
            return




# This Function checks for Game Over
def check_gameover() :
    for val in progress :
        if val == False :
            return False;

    return True




# The Game starts from here

# First print the Instructions to play the Game
print("Instructions : ")
print("1. You are given certain number of chances to Guess a secret word")
print("2. In every chance you have to enter a letter in lower case")
print("3. If the letter is present in the secret word then it is reflected the Progress-O-Meter")
print("4. If not , then nothing happens ")
print("5. Guess the word before you run out of chances to win the Game !\n")

print("Hey ! Ready to play the Game ? ")

# Ask the Player for the number of Attempts he wants to make
Attempts = Ask_Attempts()

# Now choose the secret word
Guess_Word = choose_word()

# Array to store the Progress 1 - Letter Guessed  0 - Letter Not Guessed
progress = [False] * len(Guess_Word)


# Now simulate the Game
while Attempts > 0 :

    # First Display the Progress of the Player
    disp_progress()

    # Check for Game Over
    if check_gameover() :
        break

    # Now ask the Player for a letter
    Guess_Letter = make_guess()

    # Update Progress
    update_progress(Guess_Letter)

    # Decrease the Attempts by 1
    Attempts -= 1

if check_gameover() :
    print("\nYou Win !")
else :
    print("\nSorry , You Lost.")

print("Well Played !!")