# Write and test a function that takes one argument (a year)
# and returns True if the year is a leap year, or False otherwise.
# The code uses two lists - one with the test data, and the other with the expected results.
# The code will tell you if any of your results are invalid.

def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
        return False
    elif year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("Leap year")
        return True
    else:
        print("Common year")
        return False

test_data = [1500, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")