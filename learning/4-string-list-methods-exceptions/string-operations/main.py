# Like other data types, strings have their own set of allowed operations, although
# they are quite limited compared to numbers.
#
# In general, strings can be:
#
# concatenated (together)
# replicated.

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# The first operation is performed by the + operator (note: not an addition)
# while the second by the * operator (note again: not a multiplication).
#
# The ability to use the same operator against completely different data types
# (such as numbers vs. strings) is called overloading (since such an operator
# is overloaded with different tasks).
#
# Analyze the example:
#
# The + operator used against two or more strings produces a new string containing
# all the characters of its arguments (note: order matters - this +overloaded
# in contrast to its numeric version, is not commutative)
# the * operator takes a string and a number as arguments; in this case, the order does
# not matter - you can put the number before the string, or vice versa, the result will
# be the same - a new string created by the nth replication of the argument string.


# If you want to know the ASCII/UNICODE code point value of a specific character
# you can use a function called ord() (as in ordinal).
#
# The function needs a single-character string as its argument - violating this requirement
# causes a TypeError exception, and returns a number representing the argument's code point.

# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Now assign different values to char_1 and char_2, for example, α (Greek alpha)
# and ę (a letter in the Polish alphabet); then run the code and see the result it produces.

char_3 = 'α'
char_4 = 'ę'

print(ord(char_3))
print(ord(char_4))


# If you know the code point (number) and want to obtain the corresponding character
# you can use a function called chr().
#
# The function takes a code point and returns its character.
#
# Invoking it with an invalid argument (for example, a negative or invalid code point)
# causes ValueError or TypeError exceptions.

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))


# Don't think that the immutability of a string limits your ability to operate with strings.
#
# The only consequence is that you have to remember this, and implement your code in a slightly
# different way

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# This form of code is completely acceptable, will work without circumventing Python rules
# and will bring the full Latin alphabet to your screen:
# a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# output
#
# You may wonder whether creating a new copy of a string, each time you modify its content
# worsens the code's efficiency.
#
# Yes, it gets worse. A little. However, it is not at all a problem.

# Let's start with a function called min().
#
# The function finds the minimum element of the sequence passed as an argument.
# There is one condition - the sequence (string, list, doesn't matter) cannot be empty
# or else it will throw a ValueError exception.

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# The program in Example 1 has the following output:
# A
#
# output
#
# Note: It's a capital A. Why? Remember the ASCII table - which letters occupy
# the first places - top or bottom?
#
# We have prepared two more examples to analyze: Examples 2 & 3.
#
# As you can see, they present more than just strings. The expected output looks
# like the following:
# [ ]
# 0
#
# output
#
# Note: we use square brackets to prevent space from being neglected on the screen.

# Similarly, a function called max() finds the maximum element of the sequence.

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# The output of the example program:
# z
#
# output
#
# Note: It's a lowercase z.
#
# Now let's see the max() function applied to the same data as before. See Examples 2 & 3 in the editor.
#
# The expected output is:
# [y]
# 2

