# Write a program that removes all repeating numbers from the list.
# The goal is to have a list in which all numbers do not appear more than once.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("The list with unique elements only:")
print(unique_list)