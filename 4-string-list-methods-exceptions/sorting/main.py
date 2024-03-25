# Comparison is closely related to sorting (or rather, sorting is in fact a very sophisticated case of comparison).
#
# This is a good opportunity to show you two possible ways of ordering lists containing strings. Such an operation
# is very common in the real world - whenever one sees a list of names, assets, titles, or cities, one expects
# them to be ordered.
#
# Let's assume you want to sort the following list:
#  greek = ['omega', 'alpha', 'pi', 'gamma']
#
#
# In general, Python offers two different ways of ordering lists.
#
# The first is implemented as a function called sorted().
#
# The function takes an argument (a list) and returns a new list, filled with the ordered elements of the argument.
# (Note: this description is a bit simplified compared to the actual implementation - we will discuss it later).
#
# The original list remains intact.

# See example

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)


# The snippet produces the following output:
# ['omega', 'alpha', 'pi', 'gamma']
# ['alpha', 'gamma', 'omega', 'pi']

print()

# The second method affects the list itself - no new lists are created. The sorting is performed in situ
# by the method called sort().

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

#
# The output was not changed

