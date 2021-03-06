def testRobotMovement(robot_type, room_type, delay=0.02):
    """
    Runs a simulation of a single robot of type robot_type in a 5x5 room.
    """
    import ps2_visualize
    room = room_type(5, 5)
    robot = robot_type(room, 1)
    anim = ps2_visualize.RobotVisualization(1, 5, 5, delay)
    while room.getNumCleanedTiles() < room.getNumTiles():
        robot.updatePositionAndClean()
        anim.update(room, [robot])
    anim.done()
