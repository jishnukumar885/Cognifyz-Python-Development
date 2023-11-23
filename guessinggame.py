import random

def guessing_game():

    secret_number = random.randint(1, 100)

    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number}!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guessing_game()
