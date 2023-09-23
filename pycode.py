class robot:
    def __init__(self,name,color,brand,weight):
        self.name = name
        self.color = color
        self.brand = brand
        self.weight = weight

    def introduce_self(self):
        print("my characteristics are:"  '\n    name: ' + self.name + '\n    color: ' + self.color + '\n    brand: ' + self.brand + '\n    weight: ' + self.weight)
    
r1 = robot('romina','black','lefant','500')
r1.introduce_self()
r2 = robot('alexa','gray','amazon','100')
r2.introduce_self()
