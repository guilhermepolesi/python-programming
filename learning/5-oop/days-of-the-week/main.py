# Your task is to implement a class called Weeker. Yes, your eyes do not deceive you - this name comes from the fact
# that objects of this class will be able to store and manipulate days of a week.
#
# The class constructor accepts one argument - a string. The string represents the name of the day of the week and the
# only acceptable values must come from the following set:
#
# Mon Thu Wed Thu Fri Sat Sun
#
# Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it
# yourself;
#
#     class objects must be "printable", that is, they must be able to implicitly convert to strings in the same way as
#     constructor arguments;
#     the class must be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an
#     integer and updating the day of the week stored within the object to reflect the date change by the indicated
#     number of days, forward or backward.
#     all object properties must be private;

class WeekDayError(Exception):
    pass


class Weeker:
    __week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __check_value(self, day):
        if day in self.__week_days:
            return True

        return False

    def __init__(self, day):
        if self.__check_value(day):
            self.__day = day
        else:
            raise WeekDayError

    def __str__(self):
        return f"{self.__day}"

    def add_days(self, n):
        current_index = self.__week_days.index(self.__day)
        new_index = (current_index + n) % len(self.__week_days)
        self.__day = self.__week_days[new_index]

    def subtract_days(self, n):
        current_index = self.__week_days.index(self.__day)
        new_index = (current_index + n) % len(self.__week_days)
        self.__day = self.__week_days[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
