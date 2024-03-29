# How to create your own exception
#
# The hierarchy of exceptions is not closed or finished, and you can always expand it if you want or need to create your
# own world populated with your own exceptions.
#
# It can be useful when you create a complex module that detects errors and raises exceptions, and you want the
# exceptions to be easily distinguishable from any others thrown by Python.
#
# This is done by defining your own, new exceptions as subclasses derived from predefined subclasses.
#
# Note: If you want to create an exception that will be used as a specialized case of any built-in exception, derive it
# from this only. If you want to build your own hierarchy, and don't want it closely tied to Python's exception tree
# derive it from any of the top exception classes, such as Exception.
#
# Imagine that you created a completely new arithmetic, governed by its own laws and theorems. It is clear that the
# division has also been redefined, and has to behave differently than the routine division. It is also clear that this
# new division must raise its own exception, different from ZeroDivisionError, but it is reasonable to assume that in
# some circumstances, you (or the user of your arithmetic) may want to treat all zero divisions in the same way.
#
# Requirements like these can be met. See the code, and let's analyze it:

class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')


# We define our own exception, called MyZeroDivisionError, derived from the built-in ZeroDivisionError. As you can see
# we decided not to add any new components to the class.
#
#     In effect, an exception to this class can be - depending on the desired point of view - treated as a simple
#     ZeroDivisionError, or considered separately.
#
#     The do_the_division() function raises either a MyZeroDivisionError or a ZeroDivisionError exception, depending
#     on the argument value.
#
#     The function is invoked four times in total, while the first two invocations are handled using just one except
#     branch (the most general) and the last two with two different branches, capable of distinguishing exceptions
#     (don't forget: the order of the branches makes a fundamental difference!)

# When you're going to build a completely new universe full of completely new creatures that have nothing in common
# with all the familiar things, you might want to build your own exception structure.
#
# For example, if working on a large simulation system intended to model the activities of a pizza restaurant, it may be
# desirable to form a separate hierarchy of exceptions.
#
# You can start building it by defining a general exception as a new base class for any other specialized exceptions.
# We did it as follows:

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


# Note: we will collect more specific information here than a regular Exception does, so our constructor will accept
# two arguments:
#
#     one that specifies a pizza as a process subject,
#     and one that contains a more or less precise description of the problem.
#
# As you can see, we pass the second parameter to the superclass constructor, and store the first within our own
# property.
#
# A more specific problem (such as too much cheese) may require a more specific exception. It is possible to derive the
# new class from the already defined PizzaError class, as we did here:

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


# The TooMuchCheeseError exception needs more information than the regular PizzaError exception, so we add it to the
# constructor - the name cheese is then stored for later processing.

# See the code:

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

# We combined the two previously defined exceptions and used them to work on a small example section.
#
# One of these is raised within the make_pizza() function when either of these two wrong situations are discovered:
# a wrong pizza order, or an order for too much cheese.
#
# note:
#
#     removing the branch starting with except TooMuchCheeseError will cause all exceptions that appear to be classified
#     as PizzaError;
#     Removing the branch starting with except PizzaError will cause the TooMuchCheeseError exceptions to remain
#     unhandled, and will cause the program to terminate.
#
#
# The previous solution, although elegant and efficient, has an important weakness. Due to the somewhat relaxed way of
# declaring constructors, the new exceptions cannot be used as is without a complete list of required arguments.
#
# Let's remove this weakness by setting default values for all constructor parameters. Take a look:


class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

# Now, if circumstances permit, it is possible to use class names alone.
