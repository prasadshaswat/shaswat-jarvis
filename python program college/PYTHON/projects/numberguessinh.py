import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if user_guess < number:
            print("Higher.")
        elif user_guess > number:
            print("Lower.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

guess_number()
