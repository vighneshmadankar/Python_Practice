#car selection project demo of inheritance
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod   
    def Stop():
        print("Car Stoped ...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.Stop())
print(car1.color)

