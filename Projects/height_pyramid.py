import math
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = math.floor((-1 + math.sqrt(1 + 8 * blocks))/2)

print("The height of the pyramid:", height)
