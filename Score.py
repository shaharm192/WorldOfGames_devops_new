import os
from Utils import SCORES_FILE_NAME

def calculate_points(difficulty):
    return (difficulty * 3) + 5

def add_score(difficulty):
    points = calculate_points(difficulty)
    current_score = 0

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        current_score = 0

    current_score += points

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(f"{current_score}\n")