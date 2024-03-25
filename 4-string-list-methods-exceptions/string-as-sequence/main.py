# Strings are not lists, but you can treat them as lists in many particular cases.
#
# For example, if you want to access any of the characters in a string, you can do so using
# indexing, as in the example below.

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Be careful - don't try to pass the boundaries of a string - this will cause an exception.

# Iterating through the strings also works. See the example below:

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# The output is the same as before

# slices
#
# Plus, everything you know about slices is still usable.

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# The in operator.
#
# The in operator shouldn't surprise you when applied to strings - it simply checks
# whether its left argument (a string) can be found anywhere within its right argument (another string).
#
# The check result is simply True or False.
#
# See the example program below. This is how the in operator works:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


# The not in method.
#
# As you probably suspect, the not in operator is also applicable here.
#
# That's how it works:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


# Python strings are immutable
#
# We also told you that Python strings are immutable. This is a
# very important feature. What does it means?
#
# This mainly means that the similarity of strings and lists is limited.
# Not everything that can be done with a list can be done with a string.
#
# The first important difference does not allow you to use the del statement to remove anything from a string.
#
# The example here won't work:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# del alphabet[0]
#
#
# The only thing you can do with del and a string is to remove the string as a whole. Try to do it.
#
# Python strings do not have the append() method - you cannot expand them in any way.
#
# The example below is wrong:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet.append("A")
#
#
# with the absence of the append() method, the insert() method is illegal, too:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet.insert(0, "A")

# the index() method.
#
# (it's a method, not a function) searches the sequence from the beginning in order to find the first
# element of the value specified in its argument.
#
# Note: the searched element must occur in the sequence - its absence will cause a ValueError exception.
#
# The method returns the index of the first occurrence of the argument (which means that the smallest
# possible result is 0, while the largest is the length of the argument decreased by 1).

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Therefore, the example will give the output:
# 2
# 7
# 1


# The list() function takes its argument (a string) and creates a new list containing
# all the characters in the string, one per list element.
#
# Note: it is not strictly a string function - list() is capable of creating a new list
# from many other entities (e.g. from tuples and dictionaries).

# Demonstrating the list() function:
print(list("abcabc"))

# The example output:
# ['a', 'b', 'c', 'a', 'b', 'c']


# The count() method counts all occurrences of the element within the sequence.
# The absence of such elements does not cause problems.
#
# See the second example:

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Your output is:
# 2
# 0
