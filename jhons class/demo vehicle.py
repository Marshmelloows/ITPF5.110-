class Vehicle:
    def __init__(self):
        self.colour: str = "wight"
        self.make: str = "none"
        self.power: str = "manule"
        self.wheels: int = 0

    def __str__(self):
        return f"{type(self).__name__}({self.colour}, {self.make},{self.wheels,}{self.power})"



#this is a desendint of Vehicle
#we need to make this look like a Bicyle
class Bicycle(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 2
        self.power = "peddle"
        self.colour = "black"
        self.signle = "hands"


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.make = "toyota caroler"
        self.wheels = 4
        self.power = "Gass"
        self.colour = "Red"


C = Car()
print(C)
b = Bicycle()
print(b)

