# the change in the parameter value does not propagate outside the function
# (in any case, not when the variable is a scalar).
# This also means that a function takes the value of the argument, not the argument itself.
# This is true for scalars.

# It's worth checking how it works with lists:

# The following example will shed some light on the issue:
# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
#
#
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# the code output is:
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [0, 1]
# Print #4: [2, 3]
# Print #5: [2, 3]

# Finally, you can see the difference in the example below:

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# We do not change the value of the my_list_1 parameter
# (we already know it will not affect the argument)
# but instead modify the list identified by it.

# if the argument is a list, then changing the value of the corresponding
# parameter does not affect the list (remember: variables containing lists are stored
# in a different way than scalars)
# but if you change a list identified by the parameter (note: the list, not the parameter!)
# the list will reflect the change.
