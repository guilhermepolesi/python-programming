# The continue command is used to skip the current block and advance to the next iteration
# without executing instructions inside the loop.
# Your task here is very special: you need to create a vowel eater! Write a program that uses:
# a for loop
# the concept of conditional execution (if-elif-else)
# the statement continues
# Your program must:
# ask the user to enter a word
# use user_word = user_word.upper() to convert the user-entered word to uppercase.
# use conditional execution and the continue instruction to “eat” the following vowels
# A, E, I, O, U of the introduced word;
# print the unconsumed letters to the screen, each on a separate line.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter)