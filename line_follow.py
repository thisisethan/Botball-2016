'''
function for following a black line for a given amount of time

assumes that we start on the black line when function is called
'''

BLACK_THRESHOLD = 3000;
"""value given when the IR sensor is over a black area"""

from movement import *
from decorators import timeout,TimeoutError
from wallaby import analog
IR_SENSOR_PORT = 0;
"""sensor port in which the IR sensor is located"""

def line_follow():
    while True:

        if (analog(IR_SENSOR_PORT) >= BLACK_THRESHOLD):
            move_forwards_for_time(100,100)
            turn_left_for_time(100,100)

        if (analog(IR_SENSOR_PORT) < BLACK_THRESHOLD):
            turn_right_for_time(100,100)
    """robot follows the left edge of a black line on the white board"""




def line_follow_time(time):
    try:
        timeout(time)(line_follow)()
            return 1;
    except TimeoutError:
        break
    """executes the line follow function for a given time period"""
    """takes a variable time, which is the duration the robot is to line follow"""
    """returns one if the function runs successfully"""
