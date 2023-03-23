#Cryptography Challenge #1
import random, time
#A basic encryption algorithm...
def decrypt(ciphertext, key):
 return ciphertext[::key + 1]
#  #alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  plaintext = ""
#  for i in range(0,len(ciphertext)):
#     character = ciphertext[i]
#     plaintext = plaintext + character
#  for j in range (0,key):
#     plaintext = plaintext + random.choice(alphabet)
#     return plaintext
#Main program starts here...
#Input...
ciphertext = input("Enter a message to decrypt (ciphertext): ")
key = int(input("Input a key as a number between 1 and 10: "))
while not (key>=1 and key<=10):
 print("Invalid key, try again!")
 key = int(input("Input a key as a number between 1 and 10: "))
#Process...
print("...")
print("Please, hold on")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
print("Getting it done...")
time.sleep(1)
plaintext = decrypt(ciphertext, key)
#Output...
print("plaintext:")
print(plaintext)