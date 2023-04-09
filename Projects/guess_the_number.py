secret_number = 777
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")
#print(current_time)
#if current_time >= (12:00):

# name = input(Good day)
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""
)
gn = int(input(""))
while gn != (secret_number):
    print(input("Ha ha! You're stuck in my loop!" 
                " Try again! "))
    continue
    print("Well done, muggle! You are free now.")