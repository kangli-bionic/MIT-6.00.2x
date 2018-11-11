"""6.00.2x Problem Set 2: Simulating robots."""

import math
import random

# Required code for using numpy in grader:
# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np


class Position(object):
    """Position.

    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """Initialize a position with coordinates (x, y)."""
        self._x = x
        self._y = y

    def getX(self):
        """Return x position."""
        return self._x

    def getY(self):
        """Return y position."""
        return self._y

    def getNewPosition(self, angle, speed):
        """Get new position.

        Compute and return the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Parameters
        ----------
        angle: int
            Number representing angle in degrees, 0 <= angle < 360
        speed: float
            Positive float representing speed

        Returns
        -------
        Position
            Object representing the new position.

        """
        angle = float(angle)
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))

        new_x = self.x + delta_x
        new_y = self.y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        """Return coordinates."""
        return "(%0.2f, %0.2f)" % (self._x, self._y)


class RectangularRoom(object):
    """Rectangular room.

    A RectangularRoom represents a rectangular region containing
    clean or dirty tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """Initialize a rectangular room with the specified width and height.

        Parameters
        ----------
        width: int
            width > 0
        height: int
            height > 0

        """
        self.tiles = np.zeros((width, height), dtype=int)  # All tiles are dirty (0)
        self._rows = height
        self._cols = width

    def cleanTileAtPosition(self, position):
        """Mark the tile under the position as cleaned (1).

        Parameters
        ----------
        position: Position
            Assume position is a valid position inside the room

        """
        x = math.floor(position.getX())
        y = math.floor(position.getY())
        self.tiles[x][y] = 1

    def isTileCleaned(self, m, n):
        """Return True if the tile at (m, n) has been cleaned.

        Parameters
        ----------
        m: int
        n: int
        Assumes that (m, n) represents a valid tile inside the room.

        Returns
        -------
        bool
            True if (m, n) is cleaned, False otherwise

        """
        return self.tiles[m][n] == 1

    def getNumTiles(self):
        """Get tiles count.

        Returns
        -------
        int
            Return the total number of tiles in the room.

        """
        return self.tiles.size

    def getNumCleanedTiles(self):
        """Return the total number of clean tiles in the room.

        Returns
        -------
        int
            Return the total number of clean tiles in the room.

        """
        return self.tiles[self.tiles == 1].size

    def getRandomPosition(self):
        """Return a random position inside the room.

        Returns
        -------
        Position

        """
        x = random.randint(0, self._cols - 1)
        y = random.randint(0, self._rows - 1)
        return Position(x, y)

    def isPositionInRoom(self, position):
        """Determine if a given position is in room.

        Parameters
        ----------
        position: Position

        Returns
        -------
        bool
            True if `position` is in the room, False otherwise.

        """
        return (0 <= position.getX() < self._cols) and (0 <= position.getY() < self._rows)


r = RectangularRoom(5, 8)
p = r.get_random_position()
print(p)
print(r.total_tiles_count)
# === Problem 2
# class Robot(object):
#     """
#     Represents a robot cleaning a particular room.

#     At all times the robot has a particular position and direction in the room.
#     The robot also has a fixed speed.

#     Subclasses of Robot should provide movement strategies by implementing
#     updatePositionAndClean(), which simulates a single time-step.
#     """
#     def __init__(self, room, speed):
#         """
#         Initializes a Robot with the given speed in the specified room. The
#         robot initially has a random direction and a random position in the
#         room. The robot cleans the tile it is on.

#         room:  a RectangularRoom object.
#         speed: a float (speed > 0)
#         """
#         raise NotImplementedError

#     def getRobotPosition(self):
#         """
#         Return the position of the robot.

#         returns: a Position object giving the robot's position.
#         """
#         raise NotImplementedError

#     def getRobotDirection(self):
#         """
#         Return the direction of the robot.

#         returns: an integer d giving the direction of the robot as an angle in
#         degrees, 0 <= d < 360.
#         """
#         raise NotImplementedError

#     def setRobotPosition(self, position):
#         """
#         Set the position of the robot to POSITION.

#         position: a Position object.
#         """
#         raise NotImplementedError

#     def setRobotDirection(self, direction):
#         """
#         Set the direction of the robot to DIRECTION.

#         direction: integer representing an angle in degrees
#         """
#         raise NotImplementedError

#     def updatePositionAndClean(self):
#         """
#         Simulate the passage of a single time-step.

#         Move the robot to a new position and mark the tile it is on as having
#         been cleaned.
#         """
#         raise NotImplementedError # don't change this!


# # === Problem 3
# class StandardRobot(Robot):
#     """
#     A StandardRobot is a Robot with the standard movement strategy.

#     At each time-step, a StandardRobot attempts to move in its current
#     direction; when it would hit a wall, it *instead* chooses a new direction
#     randomly.
#     """
#     def updatePositionAndClean(self):
#         """
#         Simulate the passage of a single time-step.

#         Move the robot to a new position and mark the tile it is on as having
#         been cleaned.
#         """
#         raise NotImplementedError


# # Uncomment this line to see your implementation of StandardRobot in action!
# ##testRobotMovement(StandardRobot, RectangularRoom)


# # === Problem 4
# def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
#                   robot_type):
#     """
#     Runs NUM_TRIALS trials of the simulation and returns the mean number of
#     time-steps needed to clean the fraction MIN_COVERAGE of the room.

#     The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
#     speed SPEED, in a room of dimensions WIDTH x HEIGHT.

#     num_robots: an int (num_robots > 0)
#     speed: a float (speed > 0)
#     width: an int (width > 0)
#     height: an int (height > 0)
#     min_coverage: a float (0 <= min_coverage <= 1.0)
#     num_trials: an int (num_trials > 0)
#     robot_type: class of robot to be instantiated (e.g. StandardRobot or
#                 RandomWalkRobot)
#     """
#     raise NotImplementedError

# # Uncomment this line to see how much your simulation takes on average
# ##print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# # === Problem 5
# class RandomWalkRobot(Robot):
#     """
#     A RandomWalkRobot is a robot with the "random walk" movement strategy: it
#     chooses a new direction at random at the end of each time-step.
#     """
#     def updatePositionAndClean(self):
#         """
#         Simulate the passage of a single time-step.

#         Move the robot to a new position and mark the tile it is on as having
#         been cleaned.
#         """
#         raise NotImplementedError


# def showPlot1(title, x_label, y_label):
#     """
#     What information does the plot produced by this function tell you?
#     """
#     num_robot_range = range(1, 11)
#     times1 = []
#     times2 = []
#     for num_robots in num_robot_range:
#         print("Plotting", num_robots, "robots...")
#         times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
#         times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
#     pylab.plot(num_robot_range, times1)
#     pylab.plot(num_robot_range, times2)
#     pylab.title(title)
#     pylab.legend(('StandardRobot', 'RandomWalkRobot'))
#     pylab.xlabel(x_label)
#     pylab.ylabel(y_label)
#     pylab.show()


# def showPlot2(title, x_label, y_label):
#     """
#     What information does the plot produced by this function tell you?
#     """
#     aspect_ratios = []
#     times1 = []
#     times2 = []
#     for width in [10, 20, 25, 50]:
#         height = 300//width
#         print("Plotting cleaning time for a room of width:", width, "by height:", height)
#         aspect_ratios.append(float(width) / height)
#         times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
#         times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
#     pylab.plot(aspect_ratios, times1)
#     pylab.plot(aspect_ratios, times2)
#     pylab.title(title)
#     pylab.legend(('StandardRobot', 'RandomWalkRobot'))
#     pylab.xlabel(x_label)
#     pylab.ylabel(y_label)
#     pylab.show()


# === Problem 6
# NOTE: If you are running the simulation, you will have to close it
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
