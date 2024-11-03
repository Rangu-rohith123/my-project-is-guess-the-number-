import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Guess the number (between 1 and 100)")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low, try again!")
            elif guess > number_to_guess:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
