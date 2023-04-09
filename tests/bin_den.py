def bin_to_den_conv(binary_input):
    binary_s = binary_input.split()
    binary = int(binary_s)
    den = 0
    length = len(binary)
    for i in range(length):
        if binary[i] > 1:
            print("This is not a binary number")
        else:
            den += binary[i] * 2 ** (length - 1 - i)
bin_to_den_conv(input("Enter a binary number, with each digit separated by a space: "))