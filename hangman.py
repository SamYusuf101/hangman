def guess_letter_game():
    print("Welcome to the Guess the Letters game!")
    secret_word = "david"
    guessed_letters = ["_"] * len(secret_word)
    attempts = 0
    max_attempts = 6  # Adjust this as needed
    
    # Hangman stages ASCII art
    hangman_stages = [
        
        """
           ------
           |    |
           |
           |
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ------
        """
    ]
    
    current_stage = 0
    
    while attempts < max_attempts and "_" in guessed_letters:
        print(f"You have {max_attempts - attempts} attempts left.")
        print(hangman_stages[current_stage])
        print("Current progress:", " ".join(guessed_letters))
        guess = input("Enter your guess (a letter): ").lower()
        attempts += 1
        
        if len(guess) == 1 and guess.isalpha():
            if guess in secret_word:
                print(f"Correct! '{guess}' is in the word.")
                # Update guessed_letters to reveal the guessed letter(s)
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        guessed_letters[i] = guess
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                current_stage += 1
        else:
            print("Please enter a single letter.")
    
    if "_" not in guessed_letters:
        print(f"Congratulations! You guessed the word '{secret_word}' correctly in {attempts} attempts.")
    else:
        print(f"Sorry, you've run out of attempts. The correct word was '{secret_word}'.")
        print(hangman_stages[current_stage])
    
    print("Thanks for playing!")

# Call the function to start the game
guess_letter_game()

