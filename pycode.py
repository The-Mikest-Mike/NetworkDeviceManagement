# class
class Robot: 
    number_of_robots = 0

    def __init__(self, name, color, brand, weight):
        self.name = name
        self.color = color
        self.brand = brand
        self.weight = float(weight)

        Robot.number_of_robots += 1

    # print information about their characteristics
    def introduce_self(self):
        print(f"my characteristics are:\nName: {self.name}\nColor: {self.color}\nBrand: {self.brand}\nWeight: {self.weight} kg")

        
# add robots with their characteristics
r1 = Robot('Romina', 'Black', 'Lefant', .500)
r2 = Robot('Alexa', 'Gray', 'Amazon', .100)

# print number of robots. It will be updated as robots being added
print(f"the current number of robots is: {Robot.number_of_robots}")
   
r1.introduce_self()
r2.introduce_self()



