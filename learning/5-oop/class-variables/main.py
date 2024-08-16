# Class variables
#
# A class variable is a property that exists only in a copy and is stored outside of any object.
#
# Note: There is no instance variable if there is no object in the class; a class variable exists in a copy, even if
# there are no objects in the class.
#
# Class variables are created differently than their instance siblings. The example will tell you more:

class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# Look:
#
#     there is an assignment in the first list of the class definition - it sets the variable called counter to 0;
#     initializing the variable within the class but outside any of its methods makes the variable a class variable;
#     accessing such a variable looks the same as accessing any instance attribute - you can see it in the constructor
#     body; As you can see, the constructor increments the variable by one; in effect, the variable counts all objects
#     created.
#
# Executing the code will cause the following output:
# {'_ExampleClass__first': 1} 3
# {'_ExampleClass__first': 2} 3
# {'_ExampleClass__first': 4} 3
#
# Two important conclusions come from the example:
#
#     class variables are not shown in a __dict__ object (this is natural because class variables are not parts of an
#     object) but you can always try looking for the variable of the same name but at the class level - we will show you
#     this very in brief;
#     a class variable always has the same value in all class instances (objects)


# Mangling a class variable name has the same effects as those you are already familiar with.
#
# See the example. Can you guess its output?
#
# Run the program and check if your predictions were correct. Everything works as expected, doesn't it?

class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)


# We told you before that class variables exist even when no class instance (object) has been created.
#
# Now let's take the opportunity to show you the difference between these two __dict__ variables, the class variable and
# the object variable.
#
# See the code

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)


# Let's take a closer look:
#
#     We define a class called ExampleClass;
#
#     The class defines a class variable called varies;
#
#     The class constructor sets the variable with the parameter value;
#
#     Naming the variable is the most important aspect of the example because:
#         Changing the assignment to self.varia = val would create an instance variable with the same name as the class;
#         Changing the assignment to varia = val would operate on a method's local variable; (We strongly encourage you
#         to test the two cases above - this will make it easier for you to remember the difference)
#     The first line of code outside the class prints the value of the ExampleClass.varia attribute; note - we use the
#     value before the first object of the class is instantiated.
#
# Run the code in the editor and check its output.
#
# As you can see, the __dict__ class contains much more data than its object counterpart. Most of them are useless now -
# the one we want to check carefully shows the current value varies.
#
# Note that the object's __dict__ is empty - the object has no instance variables.
