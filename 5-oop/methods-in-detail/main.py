# Methods in detail
#
# Let's summarize all the facts regarding the use of methods in Python classes.
#
# As you already know, a method is a function incorporated within a class.
#
# There is a fundamental requirement - a method is required to have at least one parameter (there are no such thing as
# parameterless methods - a method can be invoked without an argument, but not declared without parameters).
#
# The first (or only) parameter is usually called self. We suggest you follow the convention - it is commonly used, and
# will cause some surprises when using other names for it.
#
# The name self suggests the purpose of the parameter - it identifies the object for which the method is invoked.
#
# If you're going to invoke a method, you shouldn't pass the argument to the self parameter - Python will set it for you
#
# The example shows the difference.

class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()


# Code output:
# method
#
# Note the way we created the object - we treated the class name as a function, returning a newly instantiated object of the class.
#
# If you want the method to accept other self parameters, you must:
#
#     put them after self in the method definition;
#     deliver them during invocation without specifying self (as previously)
#
# Such as here:

class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

# Code output:
# method: 1
# method: 2
# method: 3


# The self parameter is used to gain access to the object instance and class variables.
#
# The example shows the two ways to use self:

class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

# Code output:
# 2 3
#
# The self function is also used to invoke other object/class methods from within the class.
#
# Such as here:

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()

# Code output:
# method
# other


# If you name a method like this: __init__, it's not a regular method - it's a constructor.
#
# If a class has a constructor, it is automatically and implicitly invoked when the class object is instantiated.
#
# The builder:
#
#     is required to have the self parameter (it is set automatically, as usual);
#     can (but is not necessary) have more parameters than just self; if this happens, the way the class name is used
#     to create the object must reflect the __init__ definition;
#     can be used to configure the object, that is, properly initialize its internal state, create instance variables
#     instantiate any other objects if their existence is necessary, etc.
#
# See the code. The example shows a very simple constructor working.

class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)


# Code output:
# object

# Note that the constructor:
#
#     it cannot return a value, as it was designed to return a newly created object and nothing else;
#     cannot be invoked directly from the object or from within the class (it can invoke a constructor from any of the
#     object's subclasses, but we will discuss this issue later).


# Since __init__ is a method, and a method is a function, you can do the same tricks with constructors/methods as you do
# with regular functions.
#
# The example shows how to define a constructor with a default argument value.

class Classy:
    def __init__(self, value=None):
        self.var = value


obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)

# Code output:
# object
# None
#
# Everything we said about property name mangling applies to method names as well - a method whose name starts with
# __ is (partially) hidden.
#
# The example shows this effect:

class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()

# Code output:
# visible
# failed
# hidden
