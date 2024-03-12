# Your task is to write a tax calculator.
# It must accept a floating-point value: the yield.
# Next, you must print the calculated tax, rounded to full thalers.
# There is a function called round() that will do the rounding for you
# If the citizen's income did not exceed 85,528 thalers
# the tax was equal to 18% of income minus 556 thalers and 2 cents (this was the so-called tax relief).
# if the income were higher than this amount
# the tax would be equal to 14,839 thalers and 2 cents, plus 32% of the excess above 85,528 thalers.
# Note: this happy country never gives money back to its citizens.
# If the calculated tax is less than zero, it just means that there is no tax (the tax is equal to zero).
# Take this into account during your calculations

income = float(input("Enter the annual income: "))
tax = 0.0

if income < 0.0:
    tax = 0.0
elif income <= 85.528:
    tax = income * 0.18 - 556.02
elif income > 85.528:
    tax = 14.839 + 0.32 * (income - 85.528)
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
