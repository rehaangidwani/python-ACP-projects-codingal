decimal = input("Enter a decimal number: ")
decimal = int(decimal)
binary = ""
while decimal > 0:
    rem = decimal % 2
    binary = binary + str(rem)  
    decimal = decimal // 2
    print("Binary number is:", binary)
