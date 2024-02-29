import random

# List of words for the game
words = ["python", "hangman", "computer", "programming", "algorithm", "developer", "code"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Main function to play the game
def main():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break
        
        if attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            print("Incorrect guess.")
            attempts -= 1

if __name__ == "__main__":
    main()
