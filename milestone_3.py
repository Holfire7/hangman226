while True:
    guess = input("Guess a letter: ")
    if guess.isalpha():
        break
    else:
        print("Invalid letter. Please enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word")
else:
    print(f"{guess} is not in the word. Try again")
