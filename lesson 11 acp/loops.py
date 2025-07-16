number = int(input("Enter a number: "))
count = 0
if number == 0:
    count = 1
else:
    while number :
        number = number // 10
        count += 1
print("Total digits:", count)