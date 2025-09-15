print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
import random
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
while attempts < max_attempts:
    user_input = input("Take a guess: ")

    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    guess = int(user_input)
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
if attempts == max_attempts:
    print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")