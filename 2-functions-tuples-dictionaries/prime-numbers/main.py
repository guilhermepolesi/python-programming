# Write a function to check whether a number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()