# We need a class capable of counting seconds. Easy? Not as much as you might think, as we will have some specific
# expectations.
#
# Read them carefully, as the class you are writing about will be used to launch rockets that carry out international
# missions to Mars. It's a big responsibility. We're counting on you!
#
# Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from
# the range [0...23] - let's use military time), minutes (from the range [0...59]) and seconds (from the range [0...59])
#
# Zero is the default value for all of the above parameters. There is no need to perform any validation checks.
#
# The class itself must provide the following facilities:
#
#     objects of the class must be "printable", that is, they must be able to implicitly convert to strings of the
#     following form: "hh:mm:ss", with leading zeros added when any of the values ​​are less than 10;
#     the class must be equipped with parameterless methods called next_second() and previous_second(), increasing the
#     time stored within the objects by +1/-1 second, respectively.
#
# Use the following tips:
#
#     all object properties must be private;
#     consider writing a separate function (not a method!) to format the time string.

class Timer:
    def __init__(self, hour=0, min=0, sec=0):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def __str__(self):
        return f"{self.__format_time(self.__hour)}:{self.__format_time(self.__min)}:{self.__format_time(self.__sec)}"

    def __format_time(self, value):
        return f"{value:02d}"

    def next_second(self):
        self.__sec += 1
        if self.__sec >= 60:
            self.__sec = 0
            self.__min += 1
            if self.__min >= 60:
                self.__min = 0
                self.__hour += 1
                if self.__hour >= 24:
                    self.__hour = 0

    def prev_second(self):
        self.__sec -= 1
        if self.__sec < 0:
            self.__sec = 59
            self.__min -= 1
            if self.__min < 0:
                self.__min = 59
                self.__hour -= 1
                if self.__hour < 0:
                    self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
