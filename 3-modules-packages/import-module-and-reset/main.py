# See the code and analyze it carefully:

# from math import sin, pi
#
# print(sin(pi / 2))
#
# pi = 3.14
#
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
#
# print(sin(pi / 2))

# line 3: perform selective import;
# line 5: make use of the imported entities and obtain the expected result (1.0)
# lines 7 to 14: redefine the meaning of pi and sin - in effect, replace the original (imported) definitions
# within the code namespace;
# line 17: get 0.99999999, which confirms our conclusions.
#
# Let's do another test. See the code below:

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))

# Here, we reverse the sequence of code operations:
#
#     lines 27 to 34: define our own pi and sin;
#     line 37: make use of them (0.99999999 appears on the screen)
#     line 39: perform the import - the imported symbols replace their previous definitions within the namespace;
#     line 41: get 1.0 as result.
