class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        log_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return log_name.title()
    
    def update_odometer(self,new_reading):
        if new_reading >= self.odometer_reading:
            self.odometer_reading = new_reading
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,increment_reading):
        self.odometer_reading += increment_reading
    
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading) + " miles on it.")
        
        
        
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This cas has a "+str(self.battery_size) + "-kWh battery." )
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh")
        else:
            print("Battery is already upgraded")
        
    
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year) # initialize attributes of parent class
        self.battery = Battery()
        