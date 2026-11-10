import random
# سازنده نیما مرتضائی
# انتخاب یک عدد تصادفی بین 1 تا 200
secret_number = random.randint(1, 200)

# تعداد فرصت های کاربر
max_attempts = 10

print("Welcome to Guess The Number Game!")
print("I have selected a number between 1 and 200.")
print(f"You have {max_attempts} attempts to guess it.")

# شروع بازی
for attempt in range(1, max_attempts + 1):

    try:
        guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

        if guess < 1 or guess > 200:
            print("Please enter a number between 1 and 200.")
            continue

        if guess == secret_number:
            print("\nCongratulations! You WON! 🎉")
            print(f"You guessed the number in {attempt} attempts.")
            break

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

    except ValueError:
        print("Invalid input! Please enter a number.")

else:
    print("\nGame Over! You LOST! 😢")
    print(f"The correct number was: {secret_number}")