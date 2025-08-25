import random

def hangman():
    # Step 1: Predefined list of words
    words = ["python", "computer", "science", "program", "hangman"]
    word = random.choice(words)  # Randomly pick a word
    guessed_word = ["_"] * len(word)  # Underscores for unguessed letters
    guessed_letters = []  # Track guessed letters
    attempts = 6  # Max incorrect guesses

    print("🎮 Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    # Step 2: Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Step 3: Check guess
        if guess in word:
            print("✅ Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(guessed_letters))

    # Step 4: End of game
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()
