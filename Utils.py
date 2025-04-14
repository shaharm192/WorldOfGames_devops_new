import os

SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = -1

# This checks if Scores.txt exists and creates it if not
def create_scores_file():
    if not os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write("0\n")

# clear the terminal screen
def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')