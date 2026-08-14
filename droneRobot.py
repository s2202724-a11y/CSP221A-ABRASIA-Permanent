from robot import Robot

class DroneRobot(Robot):
    def __init__(self, name: str, battery: int = 100, max_alt: int = 100):
        super().__init__(name, battery)
        self.max_alt = max_alt  # Added attribute for this subclass only

    def perform_task(self):
        self.use_battery(15) # Decrease cost of this subclass
        return f"{self.name} is operating at an altitude of {self.max_alt}. The battery is now at {self.battery}%."