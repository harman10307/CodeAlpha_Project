import random

# List of 5 predefined words
words = ["python", "computer", "program", "school", "coding"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Main game loop
while wrong_guesses < max_attempts:

    # Display the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the complete word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Display guessed letters
    print("Guessed letters:", guessed_letters)

    # Take input from player
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check whether letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Incorrect guesses:", wrong_guesses)
        print("Attempts remaining:", max_attempts - wrong_guesses)

# If player loses
if wrong_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")