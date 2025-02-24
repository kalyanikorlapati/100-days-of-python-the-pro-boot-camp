# 🚀 Love Calculator

print("Welcome to the Love Calculator! ❤️")

# Get user input
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

# Combine names
combined_names = name1 + name2

# Count letters for "TRUE"
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true_score = t + r + u + e

# Count letters for "LOVE"
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love_score = l + o + v + e

# Final love score
love_percentage = int(str(true_score) + str(love_score))

# ❤️ Display the result based on the score
if love_percentage < 10 or love_percentage > 90:
    print(f"Your score is {love_percentage}%, you go together like coke and mentos! 🥤💥")
elif 40 <= love_percentage <= 50:
    print(f"Your score is {love_percentage}%, you are alright together. 😊")
else:
    print(f"Your score is {love_percentage}%. 💘")
