import random

word_list = ['Mango', 'Banana', 'Watermelon', 'Pineapple', 'Guava']
word = random.choice(word_list)
print(word_list)
print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("You made a Good guess!")
else:
    print("Oops! That is not a valid input.")

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"{guess} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
    check_guess('n')
ask_for_input()