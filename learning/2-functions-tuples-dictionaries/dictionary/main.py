# Dictionary is another Python data structure
# It is not a string type (but can be easily adapted to string processing) and is mutable

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# If you want to obtain any of the values, you must provide a valid key-value:

print(dictionary['cat'])
print(phone_numbers['Suzy'])

# Obtaining the value from a dictionary resembles indexing, especially thanks
# to the square brackets surrounding the key value
# note:
# if the key is a string, you must specify it as a string
# keys are case sensitive: 'Suzy' is something different from 'suzy'

# And now the most important news: you should not use a non-existent key
# will cause a runtime error

# Fortunately, there is a simple way to avoid such a situation. The in operator
# along with its companion, not in, can save this situation
#
# The following code safely searches for some French words:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

