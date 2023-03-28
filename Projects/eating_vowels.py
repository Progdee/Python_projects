# # Prompt the user to enter a word
# # and assign it to the user_word variable.
# user_word = input("Enter a word: ")
# user_word = user_word.upper()
# for letter in user_word:
#     vowels = ["A", "E", "I", "O", "U"]
#     if letter not in vowels:
#         print(letter)
#     # Complete the body of the for loop.
#     continue

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")
user_word = user_word.upper()
for letter in user_word:
    vowels = ["A", "E", "I", "O", "U"]
    if letter not in vowels:
        word_without_vowels += letter
print(word_without_vowels)
    # Complete the body of the for loop.
    
    # Complete the body of the loop.

# Print the word assigned to word_without_vowels.
