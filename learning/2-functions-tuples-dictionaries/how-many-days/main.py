# Write and test a function that takes two arguments (a year and a month)
# and returns the number of days for a given month/year pair
# (although only February is sensitive to the year value, your function should be universal).

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

def days_in_month(year, month):
    if isinstance(month, str):
        month = month.capitalize()
        if month == "February":
            if is_year_leap(year):
                return 29
            else:
                return 28
        if month == "April" or month == "June" or month == "September" or month == "November":
            return 30
        else:
            return 31

    if isinstance(year, int):
        if month == 2:
            if is_year_leap(year):
                return 29
            else:
                return 28
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        else:
            return 31

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")