class Dog:
    species = "Canis familiaris"
    def __init__(self, breed, name):
        
        self.breed = breed
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 20)
dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Max")
dog1.display_details()
dog2.display_details()
