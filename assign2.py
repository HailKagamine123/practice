# Example of Polymorphism:
class Type:
    def type(self):
        pass

class Plant(Type):
    def type(self):
        return "Flower"

class Favorite(Type):
    def type(self):
        return "Tulips"

def make_sound(plant):
    print(plant.type())

flower = Plant()
favorite = Favorite()

make_sound(flower)  # Output: Flower
make_sound(favorite)  # Output: Tulips

















# Example of Message Passing:
class Car:
   def start_engine(self):
        print("Engine started!")

class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} is driving...")
        car.start_engine()

honda_civic = Car()
john = Driver("John")
john.drive(honda_civic)  # Output: John is driving... Engine started!