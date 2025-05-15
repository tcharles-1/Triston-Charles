#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Final Project
#
# Author:      tristonc
#
# Created:     05/10/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random  # To generate random numbers
import os      # To check if score file exists

SCORES_FILE = "scores.txt"  # Filename to store high scores

def main():
    scores = load_scores()  # Load scores from file at the start

    while True:
        # Display the main menu options
        print("\n--- Number Guessing Game ---")
        print("1. Play Game")
        print("2. Leaderboard")
        print("3. Quit")

        choice = input("Choose an option (1-3): ")  # Get user menu choice

        if choice == "1":
            player_name = input("Enter your name: ")  # Ask player for name
            max_number = choose_difficulty()           # Ask for difficulty level
            attempts = play_game(max_number)           # Play the game and get attempts
            print(f"Good job, {player_name}! You guessed it in {attempts} tries.")
            scores = update_scores(scores, player_name, attempts)  # Update score list
            save_scores(scores)                         # Save updated scores to file
        elif choice == "2":
            show_scores(scores)  # Display the leaderboard
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break               # Exit the program
        else:
            print("Please enter a valid choice (1, 2, or 3).")  # Handle invalid input

def choose_difficulty():
    while True:
        print("\nSelect difficulty:")
        print("1. Easy (1 to 10)")
        print("2. Medium (1 to 50)")
        print("3. Hard (1 to 100)")

        choice = input("Enter 1, 2, or 3: ")

        # Map user input to max number for guessing range
        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("Invalid choice. Try again.")  # Prompt again if invalid input

def play_game(max_number):
    secret_number = random.randint(1, max_number)  # Pick a random target number
    attempts = 0  # Count how many guesses the player makes

    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while True:
        guess = input("Your guess: ")

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a number.")
            continue

        guess = int(guess)  # Convert input to integer
        attempts += 1       # Increment attempts count

        # Give feedback on guess compared to secret number
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Correct!")
            return attempts  # Return attempts when guessed correctly

def load_scores():
    scores = []
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Each line contains name and attempts separated by comma
                    name, attempts_str = line.split(",")
                    scores.append((name, int(attempts_str)))
    return scores

def save_scores(scores):
    with open(SCORES_FILE, "w") as file:
        for name, attempts in scores:
            file.write(name + "," + str(attempts) + "\n")

def update_scores(scores, player_name, attempts):
    scores.append((player_name, attempts))  # Add new score to list
    scores.sort(key=lambda x: x[1])         # Sort scores by attempts (lowest first)
    return scores[:10]                       # Keep only top 10 scores

def show_scores(scores):
    if not scores:
        print("\nNo high scores yet.")  # Handle empty score list
        return

    print("\n--- High Scores ---")
    print("Rank  Name           Attempts")
    for i, (name, attempts) in enumerate(scores, start=1):
        print(f"{i:<5} {name:<14} {attempts}")

def test_functions():
    print("\nRunning tests...")

    # test if update_scores sorts correctly
    test_scores = [("Amy", 5), ("Ben", 3)]
    updated = update_scores(test_scores, "Cara", 4)
    assert updated[0] == ("Ben", 3), "Test failed: sorting order"
    assert len(updated) == 3, "Test failed: length check"

    print("All tests passed!")

if __name__ == "__main__":
    test_functions()
    main()
