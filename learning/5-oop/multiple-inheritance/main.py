# Multiple inheritance occurs when a class has more than one superclass. Syntactically, such inheritance is presented
# as a comma-separated list of superclasses placed within parentheses, after the new class name - such as here:

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

# The Sub class has two superclasses: SuperA and SuperB. This means that the Sub class inherits all the goods offered
# by both SuperA and SuperB.
#
# The code prints:
# 10 11
# 20 21
#
# Now it's time to introduce a completely new term - overriding.
#
# What do you think will happen if more than one of the superclasses defines an entity with a given name?


# Let's analyze the example:

class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

# Both Level1 and Level2 classes define a method called fun() and a property called var. Does this mean that the Level3
# class object can have access to two copies of each entity? Not at all.
#
# The entity defined later (in the sense of inheritance) overrides the same entity defined earlier. This is why the code
# produces the following output:
# 200 201
#
# As you can see, the var keyword argument and fun() method from the Level2 class replace entities with the same names
# derived from the Level1 class.
#
# This feature can be intentionally used to modify default (or previously defined) class behaviors when any of your
# classes need to act in a different way than their ancestors.
#
# We can also say that Python searches for an entity from bottom to top, and is fully satisfied with the first entity
# of the desired name.
#
# How does it work when a class has two ancestors that offer the same entity, and they are at the same level? In other
# words, what should you expect when a class emerges using multiple inheritance? Let's see this.

# Let's look at the example:

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

# The Sub class inherits assets from two superclasses, Left and Right (these names are intended to be meaningful).
#
# There is no doubt that the var_right class variable comes from the Right class, and var_left comes from Left
# respectively.
#
# This is evident. But where does var come from? Is it possible to guess it? The same problem is encountered with the
# fun() method - will it be invoked from Left or from Right? Let's run the program - its output is:
# L LL RR Left
#
# This proves that both unclear cases have a solution within the Left class. Is this a sufficient premise to formulate
# a general rule? Yes it is.
#
# We can say that Python looks for object components in the following order:
#
#     within the object itself;
#     in its superclasses, from bottom to top;
#     If there is more than one class in a given inheritance path, Python parses them from left to right.
#
# Do you need anything else? Just make a small amendment to the code - replace: class Sub(Left, Right): with: class
# Sub(Right, Left): then run the program again and see what happens.
#
# What do you see now? We see:
# R LL RR Right

