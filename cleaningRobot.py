from robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, battery: int = 100, dust_capacity: int= 50):
        super().__init__(name, battery) # Reuse the name and battery attributes from the parent class
        self.dust_capacity = dust_capacity # Added attributed for this subclass only

    def perform_task(self):
        self.battery -= 10 # Decrease cost of this subclass
        return f"{self.name} is cleaning. The battery is now at {self.battery}% and the dust capacity is {self.dust_capacity} units."