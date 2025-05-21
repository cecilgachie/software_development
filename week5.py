# Example 1: Smartphone class with inheritance and encapsulation
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._battery = 100  # Encapsulated attribute

    def use(self, amount):
        if self._battery - amount >= 0:
            self._battery -= amount
            print(f"Used {amount}% battery. Remaining: {self._battery}%")
        else:
            print("Not enough battery!")

    def charge(self):
        self._battery = 100
        print("Phone fully charged.")

    def get_battery(self):
        return self._battery

class GamingSmartphone(Smartphone):
    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model}!")
        self.use(20)

# Example 2: Vehicle classes demonstrating polymorphism
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("driving")

class Plane(Vehicle):
    def move(self):
        print("flying")

# Testing the classes
if __name__ == "__main__":
    # Smartphone example
    phone = GamingSmartphone("TechBrand", "X1000")
    phone.play_game("Space Invaders")
    phone.use(30)
    print(f"Battery left: {phone.get_battery()}%")
    phone.charge()

    # Vehicle example
    vehicles = [Car(), Plane()]
    for v in vehicles:
        v.move()