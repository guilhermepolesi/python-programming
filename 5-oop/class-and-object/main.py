# Your first class
#
# Object programming is the art of defining and expanding classes. A class is a model of a very specific part of reality
# reflecting properties and activities found in the real world.
#
# The classes defined at the beginning are too general and imprecise to cover as many real cases as possible.
#
# There is no obstacle to defining new and more precise subclasses. They will inherit everything from their superclass
# so that the work that went into their creation is not wasted.
#
# The new class can add new properties and new activities, and therefore can be more useful in specific applications.
# Obviously, it can be used as a superclass for any number of newly created subclasses.
#
# The process does not need to have an end. You can create as many classes as you need.
#
# The defining class has nothing to do with the object: the existence of a class does not mean that any of the
# compatible objects will automatically be created. The class itself cannot create an object - you have to create it
# and Python allows you to do that.
#
# It's time to define the simplest class and create an object. See the example below:
class TheSimplestClass:
    pass


#
#
# We define a class there. The class is quite poor: it has no properties or activities. It's actually empty, but that
# doesn't matter for now. The simpler the class, the better for our purposes.
#
# The definition starts with the keyword class. The keyword is followed by an identifier that gives the class its name
# (note: not to be confused with the name of the object - these are two different things).
#
# Next, add a colon (:), since classes, like functions, form their own nested block. The content inside the block
# defines all the class's properties and activities.
#
# The keyword pass fills the class with nothing. It does not contain any methods or properties.

# Your first object
#
# The newly defined class becomes a tool capable of creating new objects. The tool must be used explicitly, on request.
#
# Imagine that you want to create one (exactly one) object of the TheSimplestClass class.
#
# To do this, it is necessary to assign a variable to store the newly created object of that class, and create an object
# at the same time.
#
# Do it as follows:
my_first_object = TheSimplestClass()


#
#
# note:
#
#     the class name tries to pretend it's a function - can you see this? We will discuss this shortly;
#     the newly created object is equipped with everything the class brings; Since this class is completely empty
#     the object is also empty.
#
# The act of creating an object of the selected class is also called instantiation (since the object becomes an instance
# of the class).

# The stack - the approach to the object

# Let's start from the absolute beginning - this is how the objective stack begins:
# class Stack:
#
#
# Now, we expect two things from her:
#
#     we want the class to have a property as stack storage - we have to "install" a list inside each object of the
#     class (note: each object must have its own list - the list must not be shared between different stacks)
#     Next, we want the list to be hidden from the view of class users.
#
# How is this done?
#
# Unlike other programming languages, Python has no way of allowing you to declare such a property out of the blue.
#
# Instead, you need to add a specific statement or instruction. Properties have to be added to the class manually.
#
# How do you ensure that such activity occurs each time the new stack is created?
#
# There is a simple way to do this - it is necessary to equip the class with a specific function - its specificity is
# twofold:
#
#     it must be named strictly;
#     is invoked implicitly, when the new object is created.
#
# Such a function is called a constructor, as its general objective is to construct a new object. The constructor must
# know everything about the object's structure, and must perform all necessary initializations.
#
# Let's add a very simple constructor to the new class.

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()  # Instantiating the object.


# And now:
#
#     the constructor name is always __init__;
#     it must have at least one parameter (we will discuss this later); the parameter is used to represent the newly
#     created object - you can use the parameter to manipulate the object, and to enrich it with the necessary
#     properties; will make use of this soon;
#     note: the required parameter is usually called self - it's just a convention, but you must follow it
#     simplifies the process of reading and understanding your code.

# Note - there are no traces of constructor invocation within the code. It was invoked implicitly and automatically.
# Let's make use of it now.

# Any changes you make inside the constructor that modify the state of the self parameter will be reflected in the
# newly created object.
#
# This means that you can add any property to the object and the property will remain there until the object ends its
# life or the property is explicitly removed.
#
# Now let's add just one property to the new object - a list for a stack. Let's name it stack_list.
#
# Such as here:

class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))


# we used dotted notation, just like when we invoke methods; this is the general convention for accessing the properties
# of an object - you need to give the object a name, put a period (.) after it, and specify the name of the desired
# property; Don't use parentheses! You don't want to invoke a method - you want to access a property;
#     If you set the value of a property for the first time (as in the constructor), you are creating it; from that
#     moment on, the object has the property and is ready to use its value;
#     we did something else in the code - we tried to access the stack_list property from outside the class immediately
#     after the object was created; we want to check the current stack length - can we do it?
#
# Yes, we did it - the code produces the following output:
# 0
#
# This is not what we want from the stack. We prefer stack_list to be hidden from the outside world.
# Will this be possible?
#
# Yes, and it's simple, but not very intuitive.

# Take a look - we added two underscores before the stack_list name - nothing more:
class Stack:
    def __init__(self):
        self.__stack_list = []


stack_object = Stack()
# print(len(stack_object.__stack_list))  # this line causes AttributeError, uncomment to check


#
# The change invalidates the program.
#
# Why?
#
# When any class component has a name that starts with two underscores (__), it becomes private - this means it can
# only be accessed from within the class.
#
# You can't see it from the outside world. This is how Python implements the concept of encapsulation.
#
# Run the program to test our assumptions - an AttributeError exception should be raised.

# Now it's time for the two functions (methods) to implement the push and pop operations. Python assumes that a function
# of this type (a class activity) must be embedded within the class body - just like a constructor.
#
# We want to invoke these functions for push and pop values. This means that both must be accessible to all users of the
# class (in contrast to the previously constructed list, which is hidden from ordinary users of the class).
#
# Such a component is called public, so its name cannot begin with two (or more) underscores. There is one more
# requirement - the name must not have more than one trailing underscore. Since no trailing underscore fully satisfies
# the requirement, it can be assumed that the name is acceptable.
#
# The functions themselves are simple. Take a look:

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

# However, there is something really strange about the code. The functions look familiar, but they have more parameters
# than their procedural counterparts.
#
# Here both functions have a parameter called self in the first position of the parameter list.
#
# Is required? Yes it is.
#
# All methods must have this parameter. Plays the same role as the first constructor parameter.
#
# Allows the method to access entities (properties and activities/methods) performed by the current object. It cannot
# be omitted. Whenever Python invokes a method, it implicitly sends the current object as the first argument.
#
# This means that a method is required to have at least one parameter, which is used by Python itself - it has no
# influence on it.
#
# If your method does not require parameters, they must be specified anyway. If it is designed to process only one
# parameter, two must be specified, and the first continues to have the same role.
#
# There is one more thing that requires explanation - the way methods are invoked from within the __stack_list variable.
#
# Fortunately, it's much simpler than it seems:
#
#     the first phase delivers the object as a whole → self;
#     Next, you need to get to __stack_list list → self.__stack_list;
#     With __stack_list ready to be used, you can perform the third and final step → self.__stack_list.append(val).
#
# The class declaration is complete, and all of its components have been listed. The class is ready to be used.
