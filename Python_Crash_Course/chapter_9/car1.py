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