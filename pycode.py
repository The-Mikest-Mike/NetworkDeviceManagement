# class to represent network devices
class Device: 
    # class variable to keep track of the number of devices
    number_of_devices = 0
    # method to initialize a device with its attributes
    def __init__(self, name, color, brand, weight, swversion, ipaddress):
        self.name = name # name of device
        self.color = color # color of device
        self.brand = brand # brand of device
        self.weight = float(weight) # weight of device in kilograms
        self.swversion = (swversion) # software version of device
        self.ipaddress = (ipaddress) # ip address of device

        Device.number_of_devices += 1 # increment the number of devices

    # method to return a description of the devices
    def introduce_self(self):
        '''Return a description of the device'''
        introduce = f'Name: {self.name}\n'\
                    f'Color: {self.color}\n'\
                    f'Brand: {self.brand}\n'\
                    f'Weight: {self.weight} kg\n'\
                    f'SWVersion: {self.swversion}\n'\
                    f'IPAdress: {self.ipaddress}'
        return introduce
        
# instantiate devices with their characteristics
d1 = Device('Romina', 'Black', 'Lefant', .500, '4.7.1', '192.168.1.2')
d2 = Device('Alexa', 'Gray', 'Amazon', .100, '4.7.1', '192.168.1.3')

# print current number of devices. It will be updated as they are being added
print(f"the current number of devices is: {Device.number_of_devices}")

# print information about the devices
print('d1\n', d1.introduce_self(), '\n')
print('d2\n', d2.introduce_self(), '\n')




