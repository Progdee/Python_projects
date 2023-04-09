def message_encoder():
  text = (input("Hello! "))
  consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 
                'S', 'T', 'V' 'W', 'X', 'Y', 'Z', "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "y", "z"]
  vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
  coded = ""
  for i in range(len(text)):
              
    if letter == "A":
      letter = "1"
    elif letter == "a":
      letter = "1"
    elif letter == "E":
      letter = "2"
    elif letter == "e":
      letter = "2"
    elif letter == "I":
      letter = "3"
    elif letter == "i":
      letter = "3"
    elif letter == "O":
      letter = "4"
    elif letter == "o":
      letter = "4"
    elif letter == "U":
      letter = "5"
    elif letter == "u":
      letter = "5"        
    elif letter in consonants:
      letter = letter + "a"
    else:
      letter = letter
    coded += letter
    code = str(coded)
    print(code)
    # coded =            
    #         coded = ""
    #         if true:
    #             letters = letters + "a";
    #             coded = coded.append(letters)
    #             print(coded)     
        
    # print(text)
message_encoder()
# text = input('Enter text: ')
# #print(text)
# #
# #codey = list(reversed(text))
# #for let in codey:
# #    print(let)
# #print(str(codey))

# for letter in text:
#     if letter == "A":
#         letter = "1" #letter.replace method
#         print(letter)
#     else:
#         letter = letter + "a"
#         print(letter)
#         print(text)
# print(text)
#   #  i = 0
#    # while i < len(text):
#       #  print(i)
#         #i += 1
#        # print(text[i])
    
#       #  text[i] = text[len(text) - i - 1]
#     #print(text[i])

    