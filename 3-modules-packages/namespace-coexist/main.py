# Now we'll show you how the two namespaces (yours and the module's) can coexist.
#
# Take a look at the example in the editor window.
#
# We define our pi and sin here.

import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

# As you can see, the entities do not affect each other.
