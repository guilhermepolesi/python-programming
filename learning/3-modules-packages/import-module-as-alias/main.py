# If you use the import module variant and you don't like the name of a particular
# module (for example, it's the same as one of your already defined entities
# so qualification becomes problematic) you can give it whatever name you want - the is called aliasing.
#
# Aliasing causes the module to be identified with a different name than the original.
# This can also shorten qualified names.
#
# Creating an alias is done in conjunction with module import, and requires the following form
# of the import statement:

# import module as aliases
#
# The “module” identifies the name of the original module while the “alias” is the name you want
# to use instead of the original.
#
# Note: as is a keyword.

import math as m

print(m.sin(m.pi/2))

# Note: After successfully performing an import of an alias (alias), the original module name becomes inaccessible
# and should not be used.
#
# In turn, when you use the from module import name variant and need to change the name of the entity, you create
# an alias for the entity. This will cause the name to be replaced with the alias you choose.
#
# This is how it can be done:
# from module import name as alias
#
#
# As before, the original name (unaliased) becomes inaccessible.
#
# The name as alias phrase may be repeated - use commas to separate multiplied phrases, like this:
# from module import n as a, m as b, o as c
#
#
# The example may seem a little strange, but it works:

# from math import pi as PI, sin as sine

# print(sine(PI/2))

