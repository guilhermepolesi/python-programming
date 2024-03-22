# Let's imagine the following problem:
#
# a program is needed to evaluate students' grade point averages
# the program must ask for the student's name, followed by their unique score
# Names may be given in any order
# Entering an empty name ends data entry (note 1: Entering an empty punctuation will
# raise the ValueError exception, but don't worry about that now, you'll see how to deal
# with such cases when we talk about exceptions in the second part of the series of Python Essentials courses)
# a list of all names, along with the average assessed score, must then be issued

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# line 11: create an empty dictionary for the entered data; the student name is used as the key, while all
# associated grades are stored in a tuple (the tuple can be a dictionary value - this is not a problem)
# line 13: enter an "infinite" loop (don't worry, it will break at the right moment)
# line 14: read the student's name here
# line 15-16: if name is an empty string (), leave the loop
# line 18: ask for one of the student's scores (an integer from the range 0-10)
# line 19-20: if the entered score is not within the range of 0 to 10, leave the loop
# line 22-23: if the student's name is already in the dictionary, lengthen the tuple associated with the
# new punctuation (note the += operator)
# line 24-25: if this is a new student (unknown to the dictionary), create a new entry - its value is a tuple
# of an element containing the entered punctuation
# line 27: iterate through the sorted student names
# line 28-29: initialize the data needed to evaluate the average (sum and counter)
# line 30-32: we iterate through the tuple, taking all subsequent scores and updating the sum, along with the counter
# line 33: evaluate and print the student's name and average score
