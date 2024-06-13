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