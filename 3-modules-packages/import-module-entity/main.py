# The import syntax indicates precisely which module entity (or entities) is acceptable in the code:
# from math import pi
#
#
# The instruction consists of the following elements:
#
#     a keyword from ;
#     The name of the module to import (selectively);
#     a keyword import;
#     the name or list of names of the entity/entities being imported into the namespace.
#
# The instruction has this effect:
#
#     The listed entities (and only those) are imported from the indicated module;
#     Imported entity names are accessible without qualification.
#
# Note: No other entities are imported. Additionally, you cannot import additional entities
# using a qualification - a line like this:
# print(math.e)
#
#
# will cause an error (and it's Euler's number: 2.71828...)
#
# Let's rewrite the previous script to incorporate the new technique.

from math import sin, pi

print(sin(pi/2))

