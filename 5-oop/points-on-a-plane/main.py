# Each point located on the plane can be described as a pair of coordinates usually called x and y. We hope you are able
# to write a Python class that stores both coordinates as float numbers. Furthermore, we want objects in this class to
# evaluate the distances between any two points located on the plane.

# This is how we imagine the class:
#
#     is called Point;
#     its constructor accepts two arguments (x and y respectively), both zero, by default;
#     all property must be private;
#     the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates
#     (the coordinates are stored privately, so they cannot be accessed directly from inside the object);
#     the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the
#     point stored within the object and the other point given as a pair of floats;
#     the class provides a method called distance_from_point(point), which calculates the distance (like the previous
#     method), but the location of the other point is given as another Point class object;

import math


class Point:

    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.get_x(), point.get_y())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
