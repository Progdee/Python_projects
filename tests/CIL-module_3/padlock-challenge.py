#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-1/
def challenge_1():
    code = 0
#Update the code below to solve this challenge

    for i in range(1,41):
        code += i


    print("Code:")
    print(code)
challenge_1()
def challenge_2():
    #Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

    code = 0
#Update the code below to solve this challenge
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                
                if digit1 < digit2:
                    if digit2 < digit3:
                        code +=1
            


    print("Code:")
    print(code)
challenge_2()

def challenge_3():
    #Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

    code = 0
#Update the code below to solve this challenge
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if digit1 % 2 == 0:
                    if digit2 % 2 == 0:
                        if digit3 % 2 == 0:
                            code +=1


    print("Code:")
    print(code)
challenge_3()