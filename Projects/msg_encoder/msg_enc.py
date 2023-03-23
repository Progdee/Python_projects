
text = input('Enter text: ')
#print(text)
#letters = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V' 'W', 'X', 'Y', 'Z']
#codey = list(reversed(text))
#for let in codey:
#    print(let)
#print(str(codey))

for letter in text:
    if letter == "A":
        letter = "1" #letter.replace method
        print(letter)
    else:
        letter = letter + "a"
        print(letter)
        print(text)
print(text)
  #  i = 0
   # while i < len(text):
      #  print(i)
        #i += 1
       # print(text[i])
    
      #  text[i] = text[len(text) - i - 1]
    #print(text[i])

    