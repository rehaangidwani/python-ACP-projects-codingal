base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(exponent):
     result=result*base
print(base, "raised to the power", exponent, "is:", result)