print("HelloWorld")

import random

def generate_random_number(start, end):
    return random.randint(start, end)

def my_cool_func():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess the number!")

    secret_number = generate_random_number(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

if __name__ == "__main__":
    my_cool_func()

