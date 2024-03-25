# See the code, it's a simple example to get started.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

# The output we expect to see looks similar to this:
# Ooppsss...
# THE END.
#
# Now see the code below:

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")

# Something changed in it - we replaced ZeroDivisionError with ArithmeticError.
#
# You already know that ArithmeticError is a general class, including (among others) the ZeroDivisionError exception.
#
# Thus, the code output remains unchanged.
#
# This also means that replacing the exception name with Exception or BaseException will not change
# the program's behavior.
#
# Let's summarize:
#
# each raised exception falls into the first corresponding branch;
# the corresponding branch does not have to specify exactly the same exception - it is enough that
# the exception is more general (more abstract) than the raised exception.


# Look at the code, what will happen here?

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

# The first corresponding branch is the one containing ZeroDivisionError. This means the console will show:
# Zero division!
# THE END.
#
# Will anything change if we swap the two except branches? Like here below:

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")


# The change is radical - the code output is now:
# Arithmetic problem!
# THE END.
#
# Why, if the exception raised is the same as before?
#
# The exception is the same, but the more general exception is now listed first - it will also catch
# all zero divisions. It also means that there is no chance of any exception reaching the ZeroDivisionError branch.
# This branch is now completely inaccessible.
#
# Remember if:
#
# The order of the branches is important!
# do not put more general exceptions before more concrete exceptions;
# this will make the latter unreachable and useless;
# Furthermore, it will make your code confusing and inconsistent;
# Python will not generate any error messages regarding this issue.

# If you want to treat two or more exceptions in the same way, you can use the following syntax:
# try:
#     :
# except (exc1, exc2):
#     :
#
#
# You simply need to put all the exception names involved in a comma-separated list, and don't forget the parentheses.
#
# If an exception is raised within a function, it can be handled:
#
#     within the function;
#     outside of function;
#
# Let's start with the first variant - see the code:

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None


bad_fun(0)

print("THE END.")


# The ZeroDivisionError exception (being a concrete case of the ArithmeticError exception class) is raised within
# the bad_fun() function, and does not leave the function - the function itself takes care of it.
#
# The program outputs:
# Arithmetic problem!
# THE END.
#
# You can also let the exception propagate outside the function. Let's test it now.
#
# See the code below:

def bad_fun(n):
    return 1 / n


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# The problem has to be solved by the summoner (or the summoner's summoner, and so on).
#
# The program outputs:
# What happened? An exception was raised!
# THE END.
#
# Note: the raised exception may cross function and module boundaries, and travel through the invocation chain
# looking for a corresponding except clause capable of handling it.
#
# If there is no such clause, the exception remains unthrown, and Python solves the problem in its standard way
# terminating your code and issuing a diagnostic message.


# The raise statement raises the specified exception called exc as if it were raised in a normal (natural) way:
# raise exc
#
#
# Note: raise is a keyword.
#
# The instruction allows you:
#
# simulate the raising of real exceptions (for example, to test your handling strategy)
# partially handle an exception and make another part of the code responsible for completing the handling
# (separation of concerns).
#
# See the code, this is how you can use it in practice.

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# The program output remains unchanged.
#
# This way, you can test your exception handling routine without forcing the code to do stupid things.


# The raise statement can also be used in the following way (note the absence of the exception name):
# raise
#
#
# There is a serious restriction: this type of raise instruction can be used within the except branch only;
# using it in any other context causes an error.
#
# The statement will immediately return to raising the same exception that is currently handled.
#
# Thanks to this, you can distribute exception handling between different parts of the code.
#
# See the code:

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

# The ZeroDivisionError exception is raised twice:
#
#     first, inside the try part of the code (this is caused by zero real division)
#     second, inside the except part by the raise statement.
#
# In effect, the code outputs:
# I did it again!
# I see!
# THE END.


# Now is a good time to show you another Python statement, called assert. This is a keyword.
# assert expression
#
#
# How does it work?
#
# She evaluates the expression;
# if the expression evaluates to True, or a non-null numeric value, or a non-empty string, or any other value other
# than None, it does nothing else;
# otherwise, it automatically and immediately raises an exception called AssertionError (in this case, we say that the
# assertion failed)
#
# How can it be used?
#
# You may want to insert it into your code where you want to be absolutely safe from obviously erroneous data, and where
# you are not completely sure that the data has already been carefully examined (for example, within a function used by
# someone else)
# raising an AssertionError exception ensures that your code does not produce invalid results, and clearly shows
# the nature of the failure;
# assertions do not replace exceptions or validate data - they are their supplements.
#
# If exceptions and data validation are like careful driving, the assertion can play the role of an airbag.
#
# Let's see the assert statement in action. See the code:

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

# The program runs without failure if you enter a valid numeric value greater than or equal to zero; otherwise
# it stops and issues the following message:
# Traceback (most recent call last):
#   File ".main.py", line 4, in
#     assert x >= 0.0
# AssertionError


