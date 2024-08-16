# In 1937, a German mathematician named Lothar Collatz formulated an intriguing (as yet unproven) hypothesis
# that can be described as follows:
# take any non-negative, non-zero integer and name it c0
# if it is even, evaluate a new c0 as c0 ÷ 2
# otherwise, if it is odd, evaluate a new c0 as 3 × c0 + 1
# If c0 ≠ 1, skip to point 2.
# The hypothesis says that, regardless of the initial value of c0, it will always go to 1.
# Write a program that reads a natural number and performs the steps above, as long as c0 remains different from 1.
# We also want it to count the steps needed to reach the goal.
# Your code must also generate all intermediate values of c0.

number = int(input("Enter a number: "))

steps = 0
if number > 0:
    c0 = number
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(int(c0))

if steps != 0:
    print("steps = " + str(steps))