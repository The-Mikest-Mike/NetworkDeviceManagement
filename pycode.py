# class
class Robot:
    def __init__(self, name, color, brand, weight):

        self.name = name
        self.color = color
        self.brand = brand
        self.weight = float(weight)

    def introduce_self(self):
        #Print information about the robot's characteristics.
        print(f"my characteristics are:\nName: {self.name}\nColor: {self.color}\nBrand: {self.brand}\nWeight: {self.weight} kg")

# usage
r1 = Robot('Romina', 'Black', 'Lefant', .500)
r1.introduce_self()
r2 = Robot('Alexa', 'Gray', 'Amazon', .100)
r2.introduce_self()
