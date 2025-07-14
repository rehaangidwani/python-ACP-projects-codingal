age = int(input("Enter the student's age: "))

if age >= 10 and age <= 20:
    print("Student is allowed to join the class.")
else:
    if age %2==0:
        print("its an even number")
    else:
        print("youre age is an odd number")
    print("Student is not allowed to join the class.")