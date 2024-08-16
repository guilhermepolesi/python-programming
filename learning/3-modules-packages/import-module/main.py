# The simplest way to import a specific module is to use the import statement as follows:

# import math

# The clause contains:
#
# a keyword import;
# the name of the module that is subject to import.
#
# The statement can be located anywhere in your code, but must be placed before the first
# use of the module's entities.
#
# If you want (or have to) import more than one module, you can do so by repeating the import clause (preferably):
# import math
# import sys
#
#
# or listing the modules after the import keyword, like here:
# import math, sys
#
#
# The instruction imports two modules, first the one called math and then the second one called sys.
#
# The list of modules can be arbitrarily long.

# Look at the snippet below. This is how you qualify the names of pi and sin with the name of your source module:
# math.pi
# math.sin
#
#
# It's simple, just put:
#
#     the name of the module (e.g. math)
#     a dot (i.e., .)
#     the name of the entity (e.g. pi)
#
# Such a form clearly indicates the namespace in which the name exists.
#
# Note: Use of this qualification is mandatory if a module was imported by the import module statement.
# It doesn't matter whether any of your code and module namespace names conflict.
#
# This first example won't be very advanced - we just want to print the value of sin(½π).

import math
print(math.sin(math.pi/2))

# Note: Removing either of the two qualifications will make the code wrong. There is no other way
# to introduce mathdo namespace if you have done the following:

# import math

