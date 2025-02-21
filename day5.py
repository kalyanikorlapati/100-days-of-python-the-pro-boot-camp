import random

# Welcome message
print("Welcome to the PyPassword Generator!")

# Ask for input
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

# Lists of characters to use
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_=+[]{};:'\",.<>?/|`~")

# Generate random characters
password_list = (
    [random.choice(letters) for _ in range(letters_count)] +
    [random.choice(symbols) for _ in range(symbols_count)] +
    [random.choice(numbers) for _ in range(numbers_count)]
)

# Shuffle the password list to make it random
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

# Print the generated password
print(f"Your generated password is: {password}")

