# write a program that uses a for loop to “count mississippily” to five.
# After counting to five, the program should print the final message “Ready or not, here I come!”

import time

for i in range(1, 6):
    print(str(i) + " Mississippi")
    time.sleep(1)
print("\nReady or not, here I come!")