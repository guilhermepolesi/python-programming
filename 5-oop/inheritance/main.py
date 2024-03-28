# Inheritance is a common practice (in object programming) of passing attributes and methods of the (defined and
# existing) superclass to a newly created class called a subclass.
#
# In other words, inheritance is a way of building a new class, not from scratch, but using a repertoire of already
# defined traits. The new class inherits (and this is the key) all the existing equipment, but is capable of adding some
# new ones if necessary.
#
# Thanks to this, it is possible to build more specialized (more concrete) classes using some predefined sets of rules
# and general behaviors.
#
# The most important factor in the process is the relationship between the superclass and all its subclasses
# (note: if B is a subclass of A and C is a subclass of B, this also means that C is a subclass of A, since the
# relationship is entirely transitory).
#
# A very simple example of two-level inheritance is presented here:

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


# All classes presented are empty for now, as we are going to show you how the mutual relationships between super and
# subclasses work. We will soon fill them with content.
#
# We can say that:
#
#     The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
#     The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
#     The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.
#
# The above knowledge comes from reading the code (in other words, we know it because we can see it).
#
# Does Python know the same? Is it possible to ask Python about this? Yes it is.

# Python offers a function that is capable of identifying a relationship between two classes, and although its diagnosis
# is not complex, it can check whether a given class is a subclass of any other class.
#
# This is what it looks like:
# issubclass(ClassOne, ClassTwo)
#
#
# The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.
#
# Let's see it in action - it might surprise you. See the code. Read it carefully.

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()


# There are two nested loops. Its goal is to check all possible ordered class pairs, and print the results of the check
# to determine whether the pair matches the subclass-superclass relationship.
#
# Run the code. The program produces the following output:
# True False False
# True True False
# True True True
#
# Let's make the result more readable:
# ↓ is a subclass of → Vehicle LandVehicle TrackedVehicle
# Vehicle True False False
# LandVehicle True True False
# TrackedVehicle True True True
#
# There is an important observation to make: each class is considered as a subclass of itself.


# As you already know, an object is an incarnation of a class. This means that the object is like a cake baked using
# a recipe that is included within the class.
#
# This can generate some major problems.
#
# Let's assume you have a cake (for example, as an argument passed to your function). You want to know what recipe was
# used to make it. Why? Because you want to know what to expect from it, for example, whether it contains nuts or not
# which is crucial information for some people.
#
# Likewise, it may be crucial if the object has (or does not have) certain characteristics. In other words, whether it
# is an object of a certain class or not.
#
# This fact can be detected by the function called isinstance():
# isinstance(objectName, ClassName)
#
#
# Functions return True if the object is an instance of the class, or False otherwise.
#
# Being an instance of a class means that the object (the cake) was prepared using a recipe contained either in the
# class or in one of its superclasses.
#
# Don't forget: if a subclass contains at least the same equipment as any of its superclasses, it means that objects of
# the subclass can do the same as objects derived from the superclass, therefore it is an instance of its home class
# and any other of its superclasses.
#
# Let's test it. Analyze the code

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


# We created three objects, one for each of the classes. Then, using two nested loops, we check all possible object
# class pairs to find out whether the objects are instances of the classes.
#
# Run the code.
#
# This is what we get:
# True False False
# True True False
# True True True
#
# output
#
# Let's make the result more readable again:
# ↓ is an instance of → Vehicle LandVehicle TrackedVehicle
# my_vehicle True False False
# my_land_vehicle True True False
# my_tracked_vehicle True True True
#
# Does the table confirm our expectations?


# There's also a Python operator worth mentioning as it refers directly to objects - here it is:
# object_one is object_two
#
#
# The is operator checks whether two variables (object_one and object_two here) refer to the same object.
#
# Don't forget that variables do not store the objects themselves, but only the handles that point to Python's internal
# memory.
#
# Assigning a value from an object variable to another variable does not copy the object, but only its handle. This is
# why an operator like is can be very useful in particular circumstances.
#
# Take a look at the code. Let's analyze it:

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)


# there is a very simple class equipped with a simple constructor, creating just one property. The class is used to
# instantiate two objects. The first is then assigned to another variable, and its val property is incremented by one.
#     then the is operator is applied three times to check all possible object pairs, and all val property values are
#     also printed.
#     the last part of the code performs another experiment. After three assignments, both strings contain the same
#     texts, but these texts are stored in different objects.
#
# The code prints:
# False
# False
# True
# 1 2 1
# True False
#
# The results demonstrate that object_1 and object_3 are actually the same objects, while string_1 and string_2 are not
# despite their content being the same.
