num = int(input("Enter a number: "))
odds = [i for i in range(num) if i % 2 != 0]
evens = [i for i in range(num) if i % 2 == 0]
print("Odd numbers:", odds)
print("Even numbers:", evens)
fruits = ["apple", "banana", "mango", "cherry"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)
