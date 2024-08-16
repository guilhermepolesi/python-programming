# Instance Variables
#
# In general, a class can be equipped with two different types of data to form the properties of a class. You've seen
# one of them when we were looking at stacks.
#
# This type of class property exists when and only when it is explicitly created and added to an object. As you already
# know, this can be done during object initialization, carried out by the constructor.
#
# Furthermore, it can be done at any time in the object's life. Furthermore, any existing property can be removed at
# any time.
#
# Such an approach has some important consequences:
#
#     different objects of the same class can have different sets of properties;
#     there must be a way to reliably check whether a specific object has the property you want to use (unless you want
#     to throw an exception - it's always worth considering)
#     each object carries its own set of properties - they do not interfere with each other in any way.
#
# Such variables (properties) are called instance variables.
#
# The word instance suggests that they are closely linked to objects (which are class instances), not to the classes
# themselves. Let's take a closer look at them.
#
# Here is an example:

class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


# It needs a further explanation before we go into any other details. Take a look at the last three lines of code.
#
# Python objects, when created, are equipped with a small set of pre-defined properties and methods. Every object has
# them, whether you want them or not. One of them is a variable called __dict__ (it's a dictionary).
#
# The variable contains the names and values ​​of all properties (variables) that the object currently carries.
# We will use it to safely present the contents of an object.
#
# Let's now dive into the code:
#
#     the class named ExampleClass has a constructor, which unconditionally creates an instance variable called first
#     and sets it to the value passed through the first argument (from the class user's perspective) or the second
#     argument (from the constructor's perspective); note the default value of the parameter - any trick you can do with
#     a regular function parameter can also be applied to methods;
#
#     the class also has a method that creates another instance variable, called second;
#
#     We created three objects of the ExampleClass class, but all these instances differ:
#
#         example_object_1 only has the property named first;
#
#         example_object_2 has two properties: first and second;
#
#         example_object_3 has been enriched with a property called third while in motion, outside the class code -
#         this is possible and completely permissible.
#
# The program outputs clearly show that our assumptions are correct - here it is:
# {'first': 1}
# {'second': 3, 'first': 2}
# {'third': 5, 'first': 4}
#
# output
#
# There is an additional conclusion that must be stated here: modifying an instance variable of any object has no impact
# on all remaining objects. Instance variables are perfectly isolated from each other.


# Take a look at the modified example:

class ExampleClass:
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val=2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# It's almost the same as the previous one. The only difference is in the property names. We added two underscores (__)
# in front of them.
#
# As you know, such an addition makes the instance variable private - it becomes inaccessible from the outside world.
#
# The actual behavior of these names is a little more complicated, so let's run the program. This is the output:
# {'_ExampleClass__first': 1}
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# {'_ExampleClass__first': 4, '__third': 5}
#
# Can you see these strange names full of underscores? Where did they come from?
#
# When Python sees that it wants to add an instance variable to an object, and will do so within any of the object's
# methods, it modulates the operation as follows:
#
#     puts a class name before its name;
#     puts an additional underscore at the beginning.
#
# That's why __first becomes _ExampleClass__first.
#
# The name is now fully accessible from outside the class. You can run code like this:
# print(example_object_1._ExampleClass__first)
#
#
# and you will obtain a valid result, without errors or exceptions.
#
# As you can see, making property private is limited.
#
# Mangling will not work if you add a private instance variable outside of the class code. In this case, it will behave
# like any other property.

