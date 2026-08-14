from cleaningRobot import CleaningRobot
from droneRobot import DroneRobot
from robot import InsufficientBatteryError


# Function of fleet report
def fleet_report(robots: list):
    print("Fleet Report:")
    for robot in robots:
        print(str(robot))

# Create a test instance
cleanRobo = CleaningRobot("Testing Robot", 120, dust_capacity=40)
droneRobo = DroneRobot("Flying Robot", 80, max_alt=200)

print(cleanRobo)
print(cleanRobo.perform_task())
print(cleanRobo)  # Shows battery reduced after performing task

print(droneRobo)
print(droneRobo.perform_task())
print(droneRobo)  # Shows battery reduced after performing task

fleet = [
    cleanRobo,
    droneRobo,
    CleaningRobot("Mop", 45, dust_capacity=20),
]

fleet_report(fleet)

print("Testing InsufficientBatteryError Exception")
drone_lowBattery = DroneRobot("Low Battery Drone", battery = 5, max_alt=50)

try:
    drone_lowBattery.perform_task() # The set requirement is 15%, but only has 5%
except InsufficientBatteryError as e:
    print(f"Caught an expected error: {e}")