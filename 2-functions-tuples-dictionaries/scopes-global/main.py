# There is a special Python method that can extend the scope of a variable to include function bodies
# (even if you want to not only read the values but also modify them).

# This effect is caused by a keyword called global:
# global name
# global name1, name2, ...

# Using this keyword inside a function with the name (or names separated by commas) of a variable
# forces Python to refrain from creating a new variable inside the function - the one accessible from
# the outside will be used instead
#
# In other words, this name becomes global (it has a global scope, and it doesn't matter if it is
# the subject of reading or assigning)

def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
