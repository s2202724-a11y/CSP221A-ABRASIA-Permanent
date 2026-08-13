from cleaningRobot import CleaningRobot
from droneRobot import DroneRobot


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