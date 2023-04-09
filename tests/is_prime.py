def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num == 3:
        return True
    elif num > 3:
        sqrt = round((num ** 0.5))
        i = 0
        i += 1
        while i <= sqrt:
            if num % i == 0:
                return False
            else:
                return True
    else:
        return None
is_prime(20)
# Write your code here.
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
