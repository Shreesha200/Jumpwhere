import os
import random

if not os.path.exists("words.txt"):
    with open("words.txt", "w") as f:
        f.write("\n".join(["Hands", "Legs", "India", "Crow", "Rain", "Evaporate", "Python", "Sunshine", "Bottle", "Laptop"]))

def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        words = [line.strip().upper() for line in f if line.strip()]
    return words

def choose_word(word_list):
    return random.choice(word_list)

def play_game(word_list):
    word = choose_word(word_list)
    guessed_letters = set()
    correct_letters = set()
    attempts_left = 6

    print("\n>>> Welcome to Hangman!")
    print("_ " * len(word))

    while attempts_left > 0:
        guess = input(">>> Guess your letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            correct_letters.add(guess)
            display_word = " ".join([letter if letter in correct_letters else "_" for letter in word])
            print(display_word)

            if all(letter in correct_letters for letter in word):
                print("🎉 Congratulations! You guessed the word correctly.")
                break
        else:
            attempts_left -= 1
            print("Incorrect!")
            print(f"You have {attempts_left} chance(s) left.")
            display_word = " ".join([letter if letter in correct_letters else "_" for letter in word])
            print(display_word)

    if attempts_left == 0:
        print(f"😢 Game Over! The word was: {word}")

def hangman():
    word_list = load_words()
    while True:
        play_game(word_list)
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    hangman()
