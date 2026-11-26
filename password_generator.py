"""
🔐 Password Generator
Generate secure random passwords with customizable options
Author: Mukunth Kiruthik R S | B.Tech AI&DS, KPRIET
"""

import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, 
                     use_digits=True, use_special=True):
    """Generate a random password based on given criteria"""
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error: At least one character type must be selected!"
    
    # Ensure at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill remaining length
    remaining = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining))
    
    # Shuffle to randomize positions
    random.shuffle(password)
    return "".join(password)

def check_strength(password):
    """Check password strength and return rating"""
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    
    ratings = {
        6: ("🟢 STRONG", "Excellent password!"),
        5: ("🟡 GOOD", "Pretty secure password."),
        4: ("🟠 FAIR", "Could be stronger."),
        3: ("🔴 WEAK", "Consider adding more variety."),
    }
    
    for threshold in sorted(ratings.keys(), reverse=True):
        if score >= threshold:
            return ratings[threshold]
    return ("⚫ VERY WEAK", "Please use a stronger password!")

def main():
    print("=" * 45)
    print("🔐 SECURE PASSWORD GENERATOR")
    print("=" * 45)
    
    try:
        length = int(input("\nPassword length (8-32): "))
        length = max(8, min(32, length))
    except ValueError:
        length = 12
    
    num_passwords = int(input("How many passwords? (1-10): ") or "3")
    num_passwords = max(1, min(10, num_passwords))
    
    print(f"\n📋 Generated {num_passwords} password(s) of length {length}:\n")
    print("-" * 50)
    
    for i in range(1, num_passwords + 1):
        pwd = generate_password(length)
        strength, message = check_strength(pwd)
        print(f"  {i}. {pwd}")
        print(f"     Strength: {strength} — {message}")
        print()
    
    print("-" * 50)
    print("💡 Tip: Use a password manager to store your passwords securely!")

if __name__ == "__main__":
    main()
