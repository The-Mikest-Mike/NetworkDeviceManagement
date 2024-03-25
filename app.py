import json

# Class to represent network devices
class Device: 
    # Class variable to keep track of the number of devices
    number_of_devices = 0
    
    # Method to initialize a device with its attributes
    def __init__(self, name, model, color, brand, weight, swversion, interface):
        self.name = name  # Name of device
        self.model = model # Model of device
        self.color = color  # Color of device
        self.brand = brand  # Brand of device
        self.weight = float(weight)  # Weight of device in kilograms
        self.swversion = swversion  # Software version of device
        self.interface = interface  # IP address of device

        Device.number_of_devices += 1  # Increment the number of devices

    # Method to return a description of the device
    def introduce_self(self):
        '''Returns a description of the device'''
        introduce = f'Name: {self.name}\n'\
                    f'Model: {self.model}\n'\
                    f'Color: {self.color}\n'\
                    f'Brand: {self.brand}\n'\
                    f'Weight: {self.weight} kg\n'\
                    f'SWVersion: {self.swversion}\n'\
                    f'interface: {self.interface}'
        return introduce

# Read device characteristics from JSON file
def read_devices_from_json(filename):
    '''
    Reads device characteristics from a JSON file and returns a list of Device objects.
    Args:
        filename (str): The name of the JSON file containing device information.
    Returns:
        list: A list of Device objects containing the characteristics of each device.
    '''
    devices = []  # Initialize an empty list to store Device objects
    with open(filename, 'r') as file:  # Open the JSON file for reading
        data = json.load(file)  # Load the JSON data from the file
        for device_data in data:  # Iterate over each device's data in the JSON data
            # Create a Device object using the device's data and append it to the devices list
            device = Device(device_data['name'],device_data['model'], device_data['color'], device_data['brand'], 
                            device_data['weight'], device_data['swversion'], device_data['interface'])
            devices.append(device)  # Append the created Device object to the list
    return devices  # Return the list of Device objects containing device characteristics

# Instantiate devices from JSON file
devices = read_devices_from_json('network_devices.json')

# Print current number of devices
print(f"The current number of devices is: {Device.number_of_devices}")

for i, device in enumerate(devices, 1):
    '''
    Iterates over the list of devices and prints information about each device.
    Args:
        devices (list): A list of Device objects containing the characteristics of each device.
        i (int): Index of the device being printed, starting from 1.
        device (Device): The Device object being printed.
    '''
    print(f"Device {i}:")  # Print the index of the device
    print(device.introduce_self())  # Print the description of the device
    print()  # Print an empty line for better readability

