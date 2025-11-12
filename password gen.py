import random
import string

print("THIS PROGRAM WILL GENERATE A PASSWORD FOR YOU")  # PROGRAM INTRODUCTION

print("How long do you want your password to be? (Enter an integer number)")

while True:
    length_input = input()
    try:
        # Try to convert the input to an integer
        length = int(length_input)

        # Check if the number is positive
        if length > 0:
            break  # Exit the loop if it's a positive integer
        else:
            print("Please enter a positive integer:")
    except ValueError:
        # Catch the error if the input cannot be converted to an integer
        print("Invalid input. Please enter an integer number:")

print(f"\nYou chose a length of: {length}")

# Define the set of all possible characters for the password
# Includes lowercase letters, uppercase letters, digits, and punctuation symbols.
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
# 1. 'random.choice(characters)' selects a random character from 'characters'.
# 2. The loop 'for _ in range(length)' repeats the operation for the desired length.
# 3. The '"".join(...)' function joins all selected characters into a single string.
password = "".join(random.choice(characters) for _ in range(length))

print(f"Your newly generated password is: {password}")

