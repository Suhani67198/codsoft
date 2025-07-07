import random
import string

# Ask user for the desired password length
length = int(input("Enter the desired password length: "))

# Define character sets: letters, digits, and punctuation
letters = string.ascii_letters  # a-z, A-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # special characters

# Combine all character sets
all_chars = letters + digits + symbols

# Generate password by randomly selecting characters
password = ''.join(random.choice(all_chars) for _ in range(length))

# Display the generated password
print("Generated Password:", password)
