#define a function called repeating sentences
import time
def repeating_sentences():

#accept input from users
    text = input("Enter the sentence to be repeated: ")
    number = int(input("Enter the number of times you want it to be repeated: "))
    
     #process
    print("...")
    time.sleep(1)
    print("Getting your text ready")
    time.sleep(1)
    print("...")
    time.sleep(1)
   
    if number < 0:
            print("You have typed a negative number. Type a positive number instead.")
            number = int(input("Enter a positive number: "))
            if number == 1:
                print("Your sentence is:")
            else:
                print("Your sentences are:")
             
    elif number == 0:
        print("Number cannot be zero. Type a number greater than 0")
        number = int(input("Enter a number greater than 0: "))
        if number == 1:
                print("Your sentence is:")
        else:
            print("Your sentences are:")
            
    elif number == 1:
        print("Your sentence is:")
        
    else:
        print("Your sentences are:") 
    for i in range(number):
        print(text)
#call the function that has been defined.
repeating_sentences()