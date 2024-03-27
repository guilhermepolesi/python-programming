# Python's attitude towards object instantiation raises an important question - in contrast to other programming
# languages, all objects of the same class cannot be expected to have the same set of properties.
#
# Just like in the example. Look carefully.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
# print(example_object.b) # uncommenting this line will cause an error


# The object created by the constructor can have only one of two possible attributes: a or b.
#
# Executing the code will produce the following output:
# 1
# Traceback (most recent call last):
#   File ".main.py", line 11, in
#     print(example_object.b)
# AttributeError: 'ExampleClass' object has no attribute 'b'

# As you can see, accessing a non-existent object (class) attribute causes an AttributeError exception.


# The try-except statement gives you the opportunity to avoid problems with non-existent properties.
#
# It's easy - see the code

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass


# As you can see, this action is not very sophisticated. Essentially, we just sweep the problem under the rug.
#
# Fortunately, there is one more way to deal with the problem.
#
# Python provides a function capable of reliably checking whether any object/class contains a specified property.
# The function is called hasattr, and expects two arguments to be passed to it:
#
#     The class or object to be checked;
#     the name of the property whose existence must be reported (note: this must be a string containing the name of the
#     attribute, not just the name)
#
# The function returns True or False.
#
# This is how you can use it:

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)


# Don't forget that the hasattr() function can also operate on classes. You can use it to find out if a class variable
# is available, just like here in the example:

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))


# The function returns True if the specified class contains a given attribute, and False otherwise.
#
# Can you guess the code output? Run it to check your assumptions.
#
# And one more example - see the code below and try to predict its output:

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))


# It was successful? Run the code to check your predictions.
