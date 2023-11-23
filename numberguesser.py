import random

def number_guesser():

    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)

    print("Welcome to the Number Guesser Game!")
    print(f"I've picked a number between {lower_limit} and {upper_limit}. Try to guess it.")

  
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower_limit or guess > upper_limit:
                print(f"Please enter a number between {lower_limit} and {upper_limit}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


number_guesser()
