# Can dictionaries be queried using the for loop, like lists or tuples?
# No and yes.
# No, because a dictionary is not a sequence type - the for loop is useless with it.
# Yes, because there are simple and very effective tools that can adapt any dictionary
# to the for loop's requirements (in other words, building an intermediate link between
# the dictionary and a temporary sequence entity).
# The first of these is a method called keys(), possessed by each dictionary. The method returns
# an iterable object consisting of all the keys collected within the dictionary. Having a group of
# keys allows you to access the entire dictionary in an easy and practical way.

# Such as here:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

# Another way is based on the use of a dictionary method called items(). The method returns tuples
# (this is the first example where tuples are something more than just an example of themselves)
# where each tuple is a key-value pair.
#
# That's how it works:

for english, french in dictionary.items():
    print(english, "->", french)

# There is also a method called values(), which works similarly to keys(), but returns values.
#
# Here is a simple example:

for french in dictionary.values():
    print(french)

# Adding a new key-value pair to a dictionary is as simple as changing a value - just assign a value
# to a new, previously non-existent key.
#
# Note: this is very different behavior compared to lists, which do not allow assigning values
# to non-existent indexes.
#
# Let's add a new pair of words to the dictionary - a little strange, but still valid:

dictionary['swan'] = 'cygne'
print(dictionary)

# You can also insert an item into a dictionary using the update() method, for example:

dictionary.update({"duck": "canard"})
print(dictionary)

# Can you guess how to remove a key from a dictionary?
#
# Note: Removing a key will always cause the associated value to be removed. Values cannot
# exist without their keys.
#
# This is done with the del instruction.
# Here is the example:

del dictionary['dog']
print(dictionary)

# Note: Removing a non-existing key causes an error

# To remove the last item in a dictionary, you can use the popitem() method:

dictionary.popitem()
print(dictionary)