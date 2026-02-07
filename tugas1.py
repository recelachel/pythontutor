secret_word = "home"
guessed_letters = []
finished = False

print("Welcome to the guessing game!")

while finished == False:
    display_word = ""

    # show current word progress
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    # check if all letters are guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        finished = True
    else:
        guess = input("Guess a letter: ")

        # input validation
        if len(guess) != 1:
            print("Please enter only ONE letter.")
        else:
            guess = guess.lower()

            if guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                guessed_letters.append(guess)

                if guess in secret_word:
                    print("Correct letter!")
                else:
                    print("Wrong letter!")