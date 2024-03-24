# Let's summarize some important questions:
#
# a module is a kind of container full of functions - you can pack as many functions as you want
# into a single module and distribute it all over the world;
# Of course, it's generally a good idea not to mix functions with different areas of application
# within a module (just like in a library - no one expects scientific works to be placed among comic books)
# so group your functions carefully and name the module that contains them in a clear and intuitive way
# (for example, do not name arcade_games a module containing functions intended for partitioning
# and formatting hard drives)
# Making too many modules can cause a little confusion - sooner or later you will want to group your modules
# in exactly the same way you previously grouped functions - is there a more general container than a module?
# yes, there is - it's a package; In the world of modules, a package plays a similar role to a folder/directory
# in the world of files.

# However, there is a smarter way to use the variable. If you write a module filled with several complex functions
# you can use it to run a series of tests to verify that the functions work correctly.
#
# Each time you modify any of these functions, you can simply run the module to make sure your changes haven't broken
# the code. These tests will be omitted when the code is imported as a module.

from modules.module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

