test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1}
print("Test Dictionary:")
print(test_dict)
key = input("Enter the word you want to check the frequency of: ")
frequency = test_dict.get(key, 0)
print(f"Frequency of '{key}' is: {frequency}")
