def check_age():
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        if age % 2 == 0:
            print("The age entered is Even.")
        else:
            print("The age entered is Odd.")
    except ValueError:
        print("Value Error: Please enter a valid integer age.")
check_age()
