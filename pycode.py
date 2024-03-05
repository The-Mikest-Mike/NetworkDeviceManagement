# class
class Robot: 
    number_of_robots = 0

    def __init__(self, name, color, brand, weight, swversion, ipaddress):
        self.name = name
        self.color = color
        self.brand = brand
        self.weight = float(weight)
        self.swversion = (swversion)
        self.ipaddress = (ipaddress)

        Robot.number_of_robots += 1

    # print information about their characteristics
    def introduce_self(self):
        '''return a description of the device/robot'''
        introduce = f'Name: {self.name}\n'\
                    f'Color: {self.color}\n'\
                    f'Brand: {self.brand}\n'\
                    f'Weight: {self.weight} kg\n'\
                    f'SWVersion: {self.swversion}\n'\
                    f'IPAdress: {self.ipaddress}'
        return introduce
        
# add robots/devices with their characteristics
r1 = Robot('Romina', 'Black', 'Lefant', .500, '4.7.1', '192.168.1.2')
r2 = Robot('Alexa', 'Gray', 'Amazon', .100, '4.7.1', '192.168.1.3')

# print number of robots/devices. It will be updated as they being added
print(f"the current number of robots is: {Robot.number_of_robots}")
   
print('r1\n', r1.introduce_self(), '\n')
print('r2\n', r2.introduce_self(), '\n')




