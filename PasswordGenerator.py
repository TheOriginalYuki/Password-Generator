import random
import string

def password_generator():
    desired_length = int(input("Enter the desired password length:"))
    uppercase_letters = (input("Include uppercase letters? (y/n):").lower() == 'y')
    lowercase_letters = (input("Include lowercase letters? (y/n):").lower() == 'y')
    include_digits = (input("Include digits? (y/n):").lower() == 'y')
    include_special = (input("Include special characters? (y/n):").lower() == 'y')

    character_pool = ''
    if uppercase_letters:
        character_pool += string.ascii_uppercase
    if lowercase_letters:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if not character_pool:
        print("No character types selected. Please select at least one character type.")

    password = ''.join(random.choice(character_pool) for _ in range(desired_length))
    print(password)

if __name__ == "__main__":
    password_generator()