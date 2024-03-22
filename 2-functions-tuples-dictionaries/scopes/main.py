# A variable existing outside a function has a scope within the function bodies.

def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

# the var variable created inside the function is not the same as when defined outside it
# looks like there are two different variables with the same name;
# the function variable obscures the variable coming from the outside world.

# We can make the previous rule more precise and appropriate:
# A variable existing outside a function has a scope within the function bodies
# excluding those that define a variable with the same name.
#
# This also means that the scope of a variable existing outside a function is only
# supported when its value is obtained (reading). Assigning a value forces the creation of the function variable itself.

