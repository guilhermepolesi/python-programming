# The Beatles were one of the most popular musical groups of the 1960s and the best-selling band in history.
# Some people consider them the most influential act of the rock era.
# In fact, they were included in Time magazine's compilation of the 100 most influential people of the 20th century.
# The band went through many lineup changes, culminating in 1962 with the formation of
# John Lennon, Paul McCartney, George Harrison and Richard Starkey (better known as Ringo Starr).
# Write a program that reflects these changes and allows you to practice the concept of lists. Your task is:
# step 1: create an empty list with the name beatles
# step 2: use the append() method to add the following band members to the list:
# John Lennon, Paul McCartney and George Harrison
# step 3: use the for loop and the append() method to ask the user to add the following band members to the list:
# Stu Sutcliffe and Pete Best
# step 4: use the del statement to remove Stu Sutcliffe and Pete Best from the list;
# step 5: Use the insert() method to add Ringo Starr to the beginning of the list.

beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(len(beatles), 5):
    member = input("New member: ")
    beatles.append(member)
print("Step 3:", beatles)

del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)