import live

print("\n🎮 Welcome to the World of Games! 🎮\n")
print("Here you can find many cool games to play.")

# Get player's name
player_name = live.welcome_name()

# Load and start the game
game_result = live.load_game()

# Print final result
if game_result:
    print("\n🏆 Congratulations, you won the game! 🏆\n")
else:
    print("\n💀 Game over. Try again! 💀\n")

# End of game message
print("\nThanks for playing! Goodbye! 🎮")
