#!/usr/bin/env python3

""" module.py - an example of a Python module """

__counter = 0

# Unlike many other programming languages, Python has no means of allowing you to hide
# such variables from the eyes of module users.
#
# You can only inform your users that this is your variable, that they can read it
# but that they should not modify it under any circumstances.
#
# This is done by preceding the variable name with _ (one underscore) or __ (two underscores)
# but remember, it's just a convention. Users of your module can obey you or not.

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)


