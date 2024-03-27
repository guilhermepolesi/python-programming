# The inner life of classes and objects
#
# Every Python class and every Python object is pre-equipped with a set of useful attributes that can be used to examine
# its capabilities.
#
# You already know one of these - it's the __dict__ property.
#
# Let's look at how it handles methods - let's look at the code:

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

# Check the output carefully.
#
# Find all defined methods and attributes. Find the context in which they exist: within the object or within the class.


# __dict__ is a dictionary. Another built-in property worth mentioning is __name__, which is a string.
#
# The property contains the class name. It's nothing exciting, just a string.
#
# Note: the __name__ attribute is missing from the object - it only exists within classes.
#
# If you want to find the class of a given object, you can use a function called type(), which is capable
# (among other things) of finding a class that has been used to instantiate any object.
#
# Look at the code:

class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)


# Code output:
# Classy
# Classy
#
# Note that a statement like this:
# print(obj.__name__)
#
#
# will cause an error.

# __module__ is also a string - it stores the name of the module that contains the class definition.
#
# Let's check it - run the code:

class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)

# Code output:
# __main__
# __main__
#
# As you know, any module called __main__ is not actually a module, but the currently executing file.


# __bases__ is a tuple. The tuple contains classes (not class names) that are direct superclasses of the class.
#
# The order is the same as that used within the class definition.
#
# We'll just show you a very basic example, as we want to highlight how inheritance works.
#
# Additionally, we will show you how to use this attribute when discussing the objective aspects of exceptions.
#
# Note: only classes have this attribute - objects do not.
#
# We define a function called printbases(), designed to clearly display the contents of the tuple.
#
# See the code.

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

# Code output:
# ( object )
# ( object )
# (SuperOne SuperTwo)
#
# Note: A class without explicit superclasses points to the object (a predefined Python class) as its direct ancestor.


# Investigate classes
#
# What can you find out about classes in Python? The answer is simple - everything.
#
# Both reflection and introspection allow a programmer to do anything with every object, regardless of its provenance.
#
# Analyze the code:

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

# The function called incIntsI() takes an object of any class, scans its contents to find all integer attributes with
# names starting with i, and increments them by one.
#
# Impossible? Not at all!
#
# That's how it works:
#
#     line 1: define a very simple class...
#     lines 3 to 10: ...and fill it with some attributes;
#     line 12: this is our function!
#     line 13: scan the __dict__ attribute, searching for all attribute names;
#     line 14: if a name starts with i...
#     line 15: ...use the getattr() function to get its current value; note: getattr() takes two arguments: an object
#     and its property name (as a string), and returns the current attribute value;
#     line 16: check if the value is of type integer, and use the isinstance() function for this purpose
#     line 17: if the check goes well, increase the property value using the setattr() function; the function takes
#     three arguments: an object, the property name (as a string), and the new property value.
#
# Code output:
# {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
# {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}
#
# And, That's all!
