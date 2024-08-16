# Inheritance is not the only way to build adaptive classes. You can achieve the same goals (not always, but very often)
# using a technique called compounding.
#
# Composition is the process of composing an object using other different objects. The objects used in the composition
# provide a set of desired characteristics (properties and/or methods) so that we can say that they act as blocks used
# to build a more complicated structure.
#
# It can be said that:
#
#     inheritance extends the capabilities of a class, adding new components and modifying existing ones; in other words
#     the complete recipe is contained within the class itself and all its ancestors; the object takes all the
#     belongings of the class and makes use of them;
#     composition designs a class as a container capable of storing and using other objects (derived from other classes)
#     where each object implements a part of the behavior of a desired class.
#
# Let's illustrate the difference using the previously defined vehicles. The previous approach led us to a class
# hierarchy in which the highest class was aware of the general rules used in turning the vehicle, but did not know how
# to control the appropriate components (wheels or tracks).
#
# Subclasses have implemented this capability by introducing specialized mechanisms. Let's do (almost) the same thing
# but using composition. The class - as in the previous example - is aware of how to turn the vehicle, but the actual
# turning is done by a specialized object stored in a property called controller. The controller class is capable of
# controlling the vehicle, manipulating the relevant parts of the vehicle.
#
# Take a look - this is how it could look.

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)


# There are two classes named Tracks and Wheels - they know how to control the vehicle's direction. There is also a
# class called Vehicle that can use any of the available controllers (the two already defined, or any other defined in
# the future) - the controller is itself passed to the class during initiation.
#
# In this way, the vehicle's turning ability is composed using an external object, not implemented inside the Vehicle
# class.
#
# In other words, we have a universal vehicle and we can install both tracks and wheels on it.
#
# The code produces the following output:
# wheels: true true
# wheels: True False
# tracks: False True
# tracks: False False

