import MemoryGame
import GuessGame
import CurrencyRouletteGame

def welcome_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name.isalpha():
            print(f"Hello {name}, welcome to the world of games!")
            return name
        else:
            print("Invalid name! Please enter a valid name using only letters.")

def load_game():
    while True:
        try:
            print("\n🎮 Available Games 🎮")
            print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
            print("2. Guess Game - guess a number and see if you chose like the computer")
            print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

            game_choice = int(input("Please choose the game you want to play (1,2,3): "))

            if game_choice not in [1, 2, 3]:
                print("❌ Invalid choice! Please select 1, 2, or 3.")
                continue  # Restart loop

            difficulty = int(input("Choose difficulty (1-5): "))
            if difficulty < 1 or difficulty > 5:
                print("❌ Invalid difficulty! Please enter a number between 1 and 5.")
                continue  # Restart loop

            if game_choice == 1:
                game_result = MemoryGame.play_memory_game(difficulty)
            elif game_choice == 2:
                game_result = GuessGame.play_guess_game(difficulty)
            elif game_choice == 3:
                game_result = CurrencyRouletteGame.play_currency_roulette(difficulty)

            # Print result
            if game_result:
                print("\n🏆 Congratulations, you won the game! 🏆\n")
            else:
                print("\n💀 Game over. Try again! 💀\n")

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again not in ["yes", "y"]:
                print("\nThanks for playing! Goodbye! 🎮")
                break

        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
