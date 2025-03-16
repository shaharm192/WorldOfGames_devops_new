import random

def difficulty():
    while True:
        try:
            number = int(input("Please choose the difficulty, 1-5 when 5 is the hardest one: "))
            if 1 <= number <= 5:
                print(f"You entered: {number}")
                return number
            else:
                print("Invalid number! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number (not letters or symbols).")

def generate_number(difficulty):
    random.seed()
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            user_guess = int(input(f"Guess a number between 1 and {difficulty}: "))
            if 1 <= user_guess <= difficulty:
                return user_guess
            else:
                print(f"Invalid choice! Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input! Please enter a number (not letters or symbols).")

def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        print("🎉 Congratulations! You guessed correctly!")
        return True
    else:
        print(f"❌ Wrong guess! The correct number was {secret_number}.")
        return False

def play_guess_game(difficulty):
    secret_number = generate_number(difficulty)

    while True:
        user_guess = get_guess_from_user(difficulty)
        print(f"You guessed: {user_guess}")

        if compare_results(secret_number, user_guess):
            print("🎉 You win!")
            return True
        else:
            print("❌ You lost! Better luck next time.")
            retry = input("Do you want to try again? (yes/no): ").strip().lower()
            if retry not in ["yes", "y"]:
                return False
