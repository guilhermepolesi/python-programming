# How to build a class hierarchy
#
# The construction of a class hierarchy is not just art for art's sake.
#
# If you divide a problem between classes and decide which one should be placed at the top and which should be placed
# at the bottom of the hierarchy, you need to carefully analyze the issue, but before we show you how to do it
# (and how not to do it), we want to highlight an interesting effect. It's nothing extraordinary (it's just a
# consequence of the general rules presented previously), but remembering it can be fundamental to understanding how
# some codes work, and how the effect can be used to build a flexible set of classes.
#
# Take a look at the code. Let's analyze it:

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()


# there are two classes, named One and Two, while Two is derived from One. Nothing special. However, one thing seems
# notable - the do_it() method.
#     the do_it() method is defined twice: originally in One and subsequently in Two. The essence of the example lies
#     in the fact that it is invoked only once - within One.
#
# The question is - which of the two methods will be invoked by the last two lines of code?
#
# The first invocation appears to be simple, and it is simple, in fact - invoking doanything() from the object called
# one will obviously activate the first of the methods.
#
# The second invocation needs some attention. It's also simple if we keep in mind how Python finds class components.
# The second invocation will launch do_it() in the form existing within class Two , regardless of whether the invocation
# takes place within class One .
#
# In effect, the code produces the following output:
# do_it from One
# do_it from Two
#
# Note: the situation in which the subclass is able to modify its superclass behavior (as in the example) is called
# polymorphism. The word comes from Greek (polys: "many" and morphe, "form"), which means that one and the same class
# can take several forms depending on the redefinitions made by any of its subclasses.
#
# The method, redefined in any of the superclasses, thereby changing the behavior of the superclass, is called virtual.
#
# In other words, no class is given once and for all. The behavior of each class can be modified at any time by any of
# its subclasses.
#
# We'll show you how to use polymorphism to extend class flexibility.


# See example:

import time

class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass

    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)

# It may seem strange, but we did not use inheritance at all - just to show that it does not limit us, and we managed
# to get ours.
#
# We define two distinct classes capable of producing two different types of land vehicles. The main difference between
# them is in the way they saw. A wheeled vehicle only turns the front wheels (usually). A tracked vehicle must stop one
# of the tracks.
#
# Can you follow the code?
#
#     a tracked vehicle turns by stopping and moving on one of its tracks (this is done by the control_track() method
#     which will be implemented later)
#     a wheeled vehicle turns when its front wheels turn (this is done by the turn_front_wheels() method)
#     the turn() method uses the appropriate method for each particular vehicle.
#
# Can you see what's wrong with the code?
#
# The turn() methods seem too similar to leave them this way.
#
# Let's rebuild the code - let's introduce a superclass to bring together all the similar aspects of driving vehicles
# moving all the specific aspects to the subclasses.

# Look at the code again. This is what we did:

import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)


# we define a superclass called Vehicle, which uses the turn() method to implement a general turning scheme, while the
# turning itself is done by a method called change_direction(); note: the previous method is empty, as we will put all
# the details in the subclass (such a method is often called an abstract method, as it only demonstrates some
# possibility that will be instantiated later)
#     we defined a subclass called TrackedVehicle (note: it is derived from the Vehicle class) that instantiated the
#     change_direction() method using the specific (concrete) method called control_track()
#     respectively, the subclass named WheeledVehicle does the same trick, but uses the turn_front_wheels() method to
#     force the vehicle to turn.
#
# The most important advantage (omitting readability issues) is that this form of code allows you to implement a brand
# new turning algorithm, just by modifying the turn() method, which can be done in one place, since all vehicles will
# obey it. .
#
# This is how polymorphism helps the programmer to keep the code clean and consistent.
