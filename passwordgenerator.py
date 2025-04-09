import random
import string
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lower + upper + digits + special
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)
    password += ''.join(random.choices(all_characters, k=length - 4))
    password = ''.join(random.sample(password, len(password)))
    print("Generated Password:", password)
try:
    length = int(input("Enter the desired password length: "))
    generate_password(length)
except ValueError:
    print("Invalid input! Please enter a valid number.")