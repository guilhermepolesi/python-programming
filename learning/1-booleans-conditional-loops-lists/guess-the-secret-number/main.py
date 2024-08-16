# Ask the user to enter an integer
# Use a while loop
# Check if the number entered by the user is the same as the number chosen by the magician.
# If the user's chosen number is different from the magician's secret number
# the user should see the message "Ha ha! You're stuck in my loop!" and you will be asked to enter a number again.
# If the number entered by the user matches the number chosen by the magician
# the number should be printed on the screen and the magician should say the following words:
# "Well done, muggle! You're free now."

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input())

while number != 777:
    print("Ha ha! You're stuck in my loop!\nSo, what is the secret number?")
    number = int(input())

print("Well done, muggle! You're free now.")