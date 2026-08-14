from abc import ABC, abstractmethod

# The class of Custom Exception
class InsufficientBatteryError(Exception):
    def __init__(self, name: str, required: int, available: int):
        self.name = name
        self.required = required
        self.available = available
        super().__init__(f'{self.name} needs a battery of {self.required}% for this task to be performed, but only has {self.available}% battery available.')

# Base class for all robots
class Robot(ABC):
    manufacturer = "Dredd Industries"
    population = 0

    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self.battery = battery  # Ensuring battery life is between 0 and 100 only
        Robot.population += 1

    # Alternative Contructor to create an instance of the class from a dictionary
    @classmethod
    def from_config(cls, config: dict):
        return cls(**config)

    # Property method
    @property
    def battery(self):
        return self._battery

    # Setter method to clamp the battery life only between 0 and 100
    @battery.setter
    def battery(self, value: int):
        if value < 0:
            self._battery = 0
        elif value > 100:
            self._battery = 100
        else:
            self._battery = value

    # Custom Exception class for Insufficient Battery
    def use_battery(self, amount: int):
        if self.battery < amount:
            raise InsufficientBatteryError(self.name, amount, self.battery)
        self.battery -= amount

    def __str__(self) -> str:
        return f"{self.name} (Battery: {self.battery}%)"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, battery={self.battery})"

    # Perform a task
    @abstractmethod
    def perform_task(self):
        pass