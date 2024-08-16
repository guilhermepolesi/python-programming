# the len() function accepts tuples, and returns the number of elements contained inside
# the + operator can join tuples (we already showed you this)
# the * operator can multiply tuples as well as lists
# the in and not in operators work in the same way as in lists

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# one of the most useful properties of the tuple is its ability
# to appear on the left side of the assignment operator. You saw this phenomenon some time ago
# when you needed to find an elegant tool to swap the values of two variables.

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# Shows three tuples that interact - in effect, the values stored in them "circulate"
# t1 becomes t2, t2 becomes t3, and t3 becomes t1.
#
# Note: the example presents one more important fact: the elements of a tuple can be variables
# and not just literals. Additionally, they can be expressions if they are on the right side of the assignment operator.
