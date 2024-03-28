# How Python finds properties and methods
#
# Let's now see how Python handles inheritance methods.
#
# Take a look at the example. Let's analyze it:

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)


# there is a class called Super, which defines its own constructor, used to assign the object property, called name.
#     the class also defines the __str__() method, which makes the class capable of presenting its identity in the form
#     of clear text.
#     the class is then used as a basis to create a subclass called Sub. The Sub class defines its own constructor
#     which invokes that of the superclass. Notice how we did it: Super.__init__(self, name).
#     we explicitly named the superclass, and pointed to the method to invoke __init__(), providing all the necessary
#     arguments.
#     We instantiate an object of class Sub and print it.
#
# Code output:
# My name is Andy.
#
# output
#
# Note: As there is no __str__() method within the Sub class, the printed string must be produced within the
# Super class. This means that the __str__() method was inherited by the Sub class.


# See the code. We modified it to show you another method of accessing any entity defined within the superclass.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)

# In the last example, we explicitly named the superclass. In this example, we use the super() function, which accesses
# the superclass without needing to know its name:
# super().__init__(name)
#
#
# The super() function creates a context in which it is not necessary (and should not) pass the self argument to the
# invoked method - this is why it is possible to activate the superclass constructor using just one argument.
#
# Note: you can use this mechanism not only to invoke the superclass constructor, but also to access any of the
# resources available within the superclass.


# Let's try to do something similar, but with properties (more precisely: with class variables).
#
# Take a look at the example:

# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)

# As you can see, the Super class defines a class variable called supVar, and the Sub class defines a variable
# called subVar.
#
# Both variables are visible inside the Sub class object - that's why the code outputs:
# 2
# 1


# The same effect can be observed with instance variables - see the second example:

# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

# The Sub class constructor creates an instance variable called subVar, while the Super constructor does the same with
# a variable called supVar. As before, both variables are accessible from within the Sub class object.
#
# The program output is:
# 12
# 11
#
# Note: the existence of the variable supVar is obviously conditioned by the invocation of the Super class constructor.
# Omitting it would result in the variable being missing from the created object


# It is now possible to formulate a general statement describing Python's behavior.
#
# When trying to access the entity of any object, Python will try (in this order):
#
#     find it within the object itself;
#     find it in all classes involved in the object's line of inheritance, from bottom to top;
#
# If both of the above fail, an exception (AttributeError) is raised.
#
# The first condition may need some additional attention. As you know, all objects derived from a given class can
# have different sets of attributes, and some of the attributes can be added to the object long after its creation.
#
# The example  summarizes this in a three-level line of inheritance. Analyze it carefully.

class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())

# All the comments we've made so far are related to single inheritance, when a subclass has exactly one superclass.
# This is the most common situation (and the most recommended too).
