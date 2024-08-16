# How are exceptions handled? The word try is fundamental to the solution.
#
# Furthermore, it is also a keyword.
#
# The recipe for success is as follows:
#
#     First, you have to try to do something;
#     Next, you need to check that everything went well.
#
# But wouldn't it be better to check all the circumstances first, and then do something only if it's safe?
#
# Just like the example:

# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
#
# if second_number != 0:
#     print(first_number / second_number)
# else:
#     print("This operation cannot be done.")
#
# print("THE END.")

# Admittedly, this way may seem the most natural and understandable, but in reality this method
# does not make programming any easier. All these checks can make your code bloated and unreadable.
#
# Python prefers a completely different approach.

# View the code, this is Python's favorite approach:

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")

# note:
#
# the try keyword starts a block of code that may or may not be working correctly;
# then Python tries to perform the risky action; if it fails, an exception is raised and Python
# starts searching for a solution;
# the except keyword starts a piece of code that will be executed if something inside the try block
# goes wrong - if an exception is raised within a previous try block, it will fail here, so the code
# located after the except keyword must provide an appropriate reaction to the exception raised;
# returning to the previous nesting level ends the try-except section.

# Let's summarize this:
# try:
#     :
#     :
# except:
#     :
#     :
#
#
# In the first step, Python tries to execute all statements placed between the try: and except: statements;
# if nothing is wrong with the execution and all instructions are executed successfully, the execution jumps
# to the point after the last line of the except: block, and the execution of the block is considered complete;
# If something goes wrong inside the try: and except: block, execution immediately jumps out of the block
# and to the first statement located after the except: keyword; this means that some of the instructions in
# the block can be silently omitted.

# See the code

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

# This is the output it produces:
# 1
# Oh dear, something went wrong...
# 3
#
# output
#
# Note: the print("2") statement was lost in the process.

# This approach has one important drawback - if there is a possibility that more than one exception could
# jump to an except: branch, you may have difficulty figuring out what actually happened.
#
# Just like the code

try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")


# The message: Oh dear, something went wrong... that appears on the console says nothing about the reason
# while there are two possible causes for the exception:
#
# non-integer data entered by the user;
# an integer value equal to 0 assigned to the variable x .
#
#
# Technically, there are two ways to solve the problem:
#
# construct two consecutive try-except blocks, one for each possible exception reason (easy, but will cause
# unfavorable code growth)
# use a more advanced variant of the instruction.
#
# This is what it looks like:
# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :
#
#
# That's how it works:
#
# if the try branch raises the exc1 exception, it will be handled by the except exc1: block;
# similarly, if the try branch raises the exc2 exception, it will be handled by the except exc2: block;
# If the try branch raises any other exception, it will be handled by the unnamed except block.


# See the solution for the code:

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


# The code, when executed, produces one of the following four output variants:
#
#     If you enter a valid, non-null integer value (for example 5) it says:
#
#     0.2
#     THE END.
#
#     output
#     if you enter 0, it says:
#
#     You cannot divide by zero, sorry.
#     THE END.
#
#     output
#     If you enter any non-integer string, you will see:
#
#     You must enter an integer value.
#     THE END.
#
#     output
#     (locally on your machine) if you press Ctrl-C while the program is waiting for user input
#     (which causes an exception called KeyboardInterrupt), the program says:
#
#     Oh dear, something went wrong...
#     THE END.


# Do not forget:
#
#     except branches are searched in the same order they appear in the code;
#     should not use more than one, except a branch with a certain exception name;
#     the number of different except branches is arbitrary - the only condition is that if you use try
#     you must place at least one except (named or not) after it;
#     the except keyword should not be used without a preceding try;
#     if any of the except branches are executed, no other branches will be visited;
#     if none of the specified except branches match the raised exception, the exception remains unhandled
#     (we will discuss this shortly)
#     If an unnamed except branch exists (an unnamed exception), it must be specified as the last one.
#
# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :
#
#
# Let's continue the experiments now.
#
# See the code, we modified the previous program - we removed the ZeroDivisionError branch.
#
# What happens now if the user enters 0 as an input?

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


# Since there are no dedicated branches for division by zero, the raised exception falls into the general
# (unnamed) branch; This means that in this case the program will say:
# Oh dear, something went wrong...
# THE END.


# Let's screw up the code once again.
#
# Look at the program. This time we removed the unnamed branch.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")

# The user enters 0 once again, and:
#
# the raised exception will not be handled by ValueError - it has nothing to do with it;
# Since there is no other branch, you should see this message:
#
# Traceback (most recent call last):
# File "exc.py", line 3, in
# y = 1 / x
# ZeroDivisionError: division by zero
#
# Learned a lot about exception handling in Python.
