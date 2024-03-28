# Let's now incorporate the Point class within another class. Furthermore, we will put three points in a class
# which will allow us to define a triangle. How can we do this?
#
# The new class will be called Triangle and this is the list of our expectations:
#
#     the constructor accepts three arguments - all of them are objects of the Point class;
#     points are stored inside the object as a private list;
#     the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle
#     described by the three points; the perimeter is a sum of all leg lengths (we mention it for the record, although
#     we are sure you know it perfectly.)

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Triangle:
    def __init__(self, vertice_1, vertice_2, vertice_3):
        self.__point_list = [vertice_1, vertice_2, vertice_3]

    def perimeter(self):
        side1 = math.sqrt(
            (self.__point_list[1].get_x() - self.__point_list[0].get_x()) ** 2 +
            (self.__point_list[1].get_y() - self.__point_list[0].get_y()) ** 2)
        side2 = math.sqrt(
            (self.__point_list[2].get_x() - self.__point_list[1].get_x()) ** 2 +
            (self.__point_list[2].get_y() - self.__point_list[1].get_y()) ** 2)
        side3 = math.sqrt(
            (self.__point_list[0].get_x() - self.__point_list[2].get_x()) ** 2 +
            (self.__point_list[0].get_y() - self.__point_list[2].get_y()) ** 2)
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
