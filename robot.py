class Robot:
    def __init__(self):
        self.pos = (0, 0)
        self.direction = "E"

    def __str__(self):
        return f"{self.pos} {self.direction}"

    def move(self, command):
        for i in command:
            if i == "R" or i == "L":
                self.rotate(i)
            elif i == "G":
                self.step()

    def step(self):
        if self.direction == "E":
            x, y = self.pos
            self.pos = x+1, y
        elif self.direction == "W":
            x, y = self.pos
            self.pos = x - 1, y
        elif self.direction == "N":
            x, y = self.pos
            self.pos = x , y + 1
        elif self.direction == "S":
            x, y = self.pos
            self.pos = x , y - 1

    def rotate(self, direction):
        dir_map = {
            "LE": "N",
            "LW": "S",
            "LN": "W",
            "LS": "E",
            "RE": "S",
            "RW": "N",
            "RN": "E",
            "RS": "W"
        }

        self.direction = dir_map[f"{direction}{self.direction}"]

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        :param instructions: list of instructions
        :return: if the robot moves in a bounded circle
        working theory follows that given a stating vertex, if the robot performs a movement sequence
        at least 4 times, it should return to it's starting position. By looping the sequence 4 time and then checking
        the robots position, it should tell us if the robot moves in a bounded circle.
        This requires the use of a robot class and a move, rotate and step function
        """
        robot = Robot()
        for i in range(4):
                robot.move(instructions)
        return robot.pos == (0, 0) and robot.direction == "E"
