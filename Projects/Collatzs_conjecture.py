#This is an iteration that gives 1 as the final result no matter what number
#you input.

#ask the user to input a natural number
c0 = int(input("Enter a natural number: "))
while c0 < 1:
    print(int(input("Please, enter a natural number: ")))

else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
            print(c0)
        else:
            c0 = 3 * c0 + 1
            print(c0)
    # c0 = int(input())
    # if c0 < 1:
    #     print("Please, enter a natural number: ")
    #     c0 = int(input())
    # else:
    #     while c0 != 1:
    #         if c0 % 2 == 0:
    #             c0 = c0 // 2
    #             print(c0)
    #         else:
    #             c0 = 3 * c0 + 1
    #             print(c0)

# else:
#     while c0 != 1:
#         if c0 % 2 == 0:
#             c0 = c0 // 2
#             print(c0)
#         else:
#             c0 = 3 * c0 + 1
#             print(c0)

