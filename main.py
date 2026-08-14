from cleaningRobot import CleaningRobot
from droneRobot import DroneRobot
from robot import InsufficientBatteryError
import logging

# The configure of logging so it runs an output to the terminal
logging.basicConfig(level=logging.INFO)


# Function of fleet report
def fleet_report(robots: list):
    print("Fleet Report:")
    for robot in robots:
        print(str(robot))

# The Task Runner Function of Full try/except/else/finally
def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)
    except InsufficientBatteryError as e:
        logging.error(f"The tasked failed: {e}")
    else:
        logging.info(f"Task completed successfully: {result}")
    finally:
        print(f"Status of {robot.name}: Battery at {robot.battery}%")

# Create a test instance
if __name__ == "__main__":
    # Test instances
    cleanRobo = CleaningRobot("Testing Robot", 100, dust_capacity=40)
    drone_lowBattery = DroneRobot("Low Battery Drone", battery=5, max_alt=50)

    print("\n--- Testing run_task_safely (Successful Run) ---")
    run_task_safely(cleanRobo)

    print("\n--- Testing run_task_safely (Battery Depleted Run) ---")
    run_task_safely(drone_lowBattery)