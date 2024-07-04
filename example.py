#Classes
class Cat:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    #Define a method
    def speak(self):
        return f"{self.name} says Meeoow"
    
    #Create the object, an instantation of a class
cat_1 = Cat("Dorica", 5, "sussex")

print(f"My cat {cat_1.name} says meeoow")