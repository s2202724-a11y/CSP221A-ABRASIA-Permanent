import logging
from cleaningRobot import CleaningRobot
from droneRobot import DroneRobot
from robot import InsufficientBatteryError

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


# Demonstration of Mutable Class Attribute Trap
def demonstrate_mutable_trap():
    # Buggy class showing shared mutable attribute
    class BuggyFleet:
        inventory = []  # Shared class-level list

    robot1 = BuggyFleet()
    robot2 = BuggyFleet()
    robot1.inventory.append("Laser Module")

    print("[BUGGY VERSION]")
    print(f"Robot 1 Inventory: {robot1.inventory}")
    print(f"Robot 2 Inventory: {robot2.inventory}")
    print(
        f"Sharing the same list? {robot1.inventory is robot2.inventory}"
    )

    # Corrected class showing independent instance attributes
    class CorrectedFleet:
        def __init__(self):
            self.inventory = []  # Independent instance-level list

    robot3 = CorrectedFleet()
    robot4 = CorrectedFleet()
    robot3.inventory.append("Laser Module")

    print("\n[CORRECTED VERSION]")
    print(f"Robot 3 Inventory: {robot3.inventory}")
    print(f"Robot 4 Inventory: {robot4.inventory}")
    print(
        f"Sharing the same list? {robot3.inventory is robot4.inventory}"
    )


# Create a test instance
if __name__ == "__main__":
    # Test instances
    cleanRobo = CleaningRobot("Testing Robot", 100, dust_capacity=40)
    drone_lowBattery = DroneRobot("Low Battery Drone", battery=5, max_alt=50)

    print("\n--- Testing run_task_safely (Successful Run) ---")
    run_task_safely(cleanRobo)

    print("\n--- Testing run_task_safely (Battery Depleted Run) ---")
    run_task_safely(drone_lowBattery)

    # Testing Decorator
    print("\n--- Testing @log_action Decorator Metadata ---")
    print(
        f"Method Name: {CleaningRobot.perform_task.__name__}"
    )  # Should print 'perform_task'

    # Testing Alternative Constructor
    print("\n--- Testing from_config Class Method ---")
    config_data = {"name": "Aqua-Drone", "battery": 15, "max_alt": 120}

    # Construct instance directly from dictionary
    drone_from_dict = DroneRobot.from_config(config_data)

    print(f"Created object: {repr(drone_from_dict)}")
    print(f"Is DroneRobot? {isinstance(drone_from_dict, DroneRobot)}")

    # Testing Mutable Class Attribute Trap
    print("\n--- Testing Mutable Class Attribute Trap ---")
    demonstrate_mutable_trap()