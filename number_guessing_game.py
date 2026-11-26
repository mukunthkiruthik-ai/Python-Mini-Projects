"""
🔢 Number Guessing Game
Guess the randomly generated number within limited attempts!
Author: Mukunth Kiruthik R S | B.Tech AI&DS, KPRIET
"""

import random

def play_game():
    """Main game function"""
    print("=" * 40)
    print("🎯 NUMBER GUESSING GAME")
    print("=" * 40)
    
    # Difficulty levels
    print("\nChoose difficulty:")
    print("1. Easy   (1-50,  10 attempts)")
    print("2. Medium (1-100,  7 attempts)")
    print("3. Hard   (1-200,  5 attempts)")
    
    choice = input("\nYour choice (1/2/3): ")
    
    levels = {
        "1": (50, 10, "Easy"),
        "2": (100, 7, "Medium"),
        "3": (200, 5, "Hard")
    }
    
    max_num, max_attempts, level_name = levels.get(choice, (100, 7, "Medium"))
    secret = random.randint(1, max_num)
    
    print(f"\n🎮 Level: {level_name}")
    print(f"I'm thinking of a number between 1 and {max_num}")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} → Your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
        
        if guess == secret:
            print(f"\n🎉 CONGRATULATIONS! You guessed it in {attempt} attempt(s)!")
            if attempt <= 3:
                print("🏆 Amazing! You're a genius!")
            elif attempt <= 5:
                print("👏 Great job! Well played!")
            else:
                print("✅ You got it! Close one!")
            return
        elif guess < secret:
            print("📈 Too LOW! Try higher.")
        else:
            print("📉 Too HIGH! Try lower.")
        
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"   ({remaining} attempts remaining)\n")
    
    print(f"\n😔 Game Over! The number was {secret}.")
    print("Better luck next time! 🍀")

def main():
    """Game loop with replay option"""
    while True:
        play_game()
        replay = input("\n🔄 Play again? (y/n): ").lower()
        if replay != 'y':
            print("\nThanks for playing! 👋")
            break
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    main()
