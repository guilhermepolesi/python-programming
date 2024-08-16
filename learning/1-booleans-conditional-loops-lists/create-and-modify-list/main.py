# Once upon a time there was a hat. The hat did not contain any rabbits, but a list of five numbers: 1, 2, 3, 4 and 5.
# Your task is:
# write a line of code that asks the user to replace the middle number in the list with a user-entered integer (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

number = int(input("Enter a number: "))

hat_list[2] = number
del hat_list[-1]
print("List length: " + str(len(hat_list)))

print(hat_list)