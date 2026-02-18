"""
Project: Number Guessing Game
==============================

A simple game where the computer picks a random number
and the player tries to guess it.

This project practices:
- Random number generation
- While loops
- User input
- Conditionals
- Variables
"""

import random

def play_game():
    """Main game function"""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    # Choose difficulty
    print("\nChoose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    
    difficulty = input("\nEnter your choice (1-3): ")
    
    if difficulty == '1':
        max_num = 50
    elif difficulty == '2':
        max_num = 100
    elif difficulty == '3':
        max_num = 200
    else:
        print("Invalid choice! Using Medium difficulty.")
        max_num = 100
    
    # Generate random number
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print("Can you guess it?\n")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > max_num:
                print(f"Please guess a number between 1 and {max_num}!")
                continue
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempts.")
                
                # Score based on attempts
                if attempts <= 3:
                    print("Amazing! You're a guessing master!")
                elif attempts <= 7:
                    print("Great job!")
                else:
                    print("You got it! Keep practicing!")
                break
                
        except ValueError:
            print("Please enter a valid number!")
    
    # Play again?
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        play_game()
    else:
        print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()
