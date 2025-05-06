import random

class CowsAndBulls:
    def __init__(self):
        self.secret = self.generate_number()
        self.guess_count = 0

    def generate_number(self):
        digits = list("0123456789")
        random.shuffle(digits)
        if digits[0] == '0':
            digits[0], digits[1] = digits[1], digits[0]
        return ''.join(digits[:4])

    def get_cows_and_bulls(self, guess):
        cows = sum(1 for i in range(4) if guess[i] == self.secret[i])
        bulls = sum(1 for i in range(4) if guess[i] in self.secret and guess[i] != self.secret[i])
        return cows, bulls

    def is_valid_guess(self, guess):
        return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4

    def play(self):
        print("Welcome to the Cows and Bulls Game!")
        while True:
            guess = input("Enter a 4-digit number with non-repeating digits: ")
            if not self.is_valid_guess(guess):
                print("Invalid input! Please enter a 4-digit number with unique digits.")
                continue

            self.guess_count += 1
            cows, bulls = self.get_cows_and_bulls(guess)

            if cows == 4:
                print(f"Congratulations! You guessed the number {self.secret} in {self.guess_count} guesses.")
                break
            else:
                print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    game = CowsAndBulls()
    game.play()
