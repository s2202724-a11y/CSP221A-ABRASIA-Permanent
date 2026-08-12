from robot import Robot
# Testinggg
class CleaningRobot(Robot):
    def perform_task(self):
        return f"{self.name} is cleaning the house."

robot = CleaningRobot("Testing Robot", 120)

print(robot)
print(robot.perform_task())