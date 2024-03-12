# Write a program that reads the number of blocks the builders have and that outputs the height of the pyramid
# that can be built using those blocks.
# The pyramid is stacked according to a simple principle: each lower layer contains one more block than the upper layer.
# Note: Height is measured by the number of completely filled layers
# if the builders don't have enough blocks and can't complete the next layer, they stop work immediately.

blocks = int(input("Enter the number of blocks: "))

height = 0
count = 0
while count < blocks:
    height += 1
    count += height
    if count > blocks:
        height -= 1
        break

print("The height of the pyramid:", height)