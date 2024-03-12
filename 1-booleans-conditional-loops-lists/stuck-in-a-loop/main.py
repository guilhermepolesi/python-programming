# The break command is used to exit/end a loop.
# Create a program that uses a while loop and continually prompts the user to enter a word
# unless the user enters "chupacabra" as the secret output word; in this case, the message
# "You have successfully exited the loop." should be printed on the screen and the loop should end.
# Do not print any of the words entered by the user.
# Use the concept of conditional execution and the break statement.

word = input("Type a word: ")

while word != "chupacabra":
    word = input("Type a word: ")
    if word == "chupacabra":
        print("\nYou've successfully left the loop.")
        break