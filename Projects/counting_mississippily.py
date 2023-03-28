import time
number = int(input("Enter the number of seconds you want to count: "))
print("...")
time.sleep(1)
print("Your time starts now!")
time.sleep(0.2)
for i in range(0,number):
    print(i+1, " mississippi")
    time.sleep(1)
print("Time up!")