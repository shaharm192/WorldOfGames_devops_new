import random
import time
import sys


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    print("\nEnter the numbers you remember, one at a time:")
    user_numbers = []

    for i in range(difficulty):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                user_numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

    return user_numbers


def is_list_equal(generated_list, user_list):
    return generated_list == user_list


def clear_screen():
    time.sleep(0.7)  # Wait before clearing
    print("\n" * 100)  # Get down 100 lines so user won't see the list of numbers
    sys.stdout.flush()


def play_memory_game(difficulty):
    numbers = generate_sequence(difficulty)
    print("\nMemorize the following numbers:")
    print(", ".join(map(str, numbers)))
    clear_screen()
    user_numbers = get_list_from_user(difficulty)

    if is_list_equal(numbers, user_numbers):
        print("🎉 Congratulations! You remembered all numbers correctly!")
        return True
    else:
        print(f"❌ Incorrect! The correct sequence was: {', '.join(map(str, numbers))}")
        return False

