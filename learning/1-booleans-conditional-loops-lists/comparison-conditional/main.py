# Write a program that uses the concept of conditional execution, takes a string as input and:
# prints the phrase "Yes - Spathiphyllum is the best plant ever!"
# to the screen if the character string entered is "Spathiphyllum" (upper case)
# prints the phrase "No, I want a big Spathiphyllum!" if the string entered is "spathiphyllum" (lower case)
# prints the phrase "Spathiphyllum! No [entry]!" otherwise. Note: [input] is the string considered as input.

plant_name = input("Enter the name of the plant: ")

if plant_name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant_name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! No " + plant_name + "!")