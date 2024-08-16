# Since the introduction of the Gregorian calendar (in 1582)
# the following rule has been used to determine the type of year:
# if the year number is not divisible by four, it is a common year
# otherwise, if the year number is not divisible by 100, it is a leap year
# otherwise, if the year number is not divisible by 400, it is a common year
# otherwise, it is a leap year.
# The code must generate one of two possible messages, which are Leap Year or Common Year
# depending on the value entered.
# It would be good to check if the year entered falls in the Gregorian era and issue a warning otherwise:
# Outside the Gregorian calendar period.

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")