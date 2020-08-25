#!/usr/bin/env python3
"""Motor node definition."""

import rospy
from drivers.msg import WheelsSpeed
from utils.motors import Motors


class MotorNode:
    """Node to control Motors.

    Subscribes to ~velocities to get motor command.
    """

    def __init__(self, node_name):
        """Initialise node.

        Args:
            node_name: Default name of the node.
        """
        # Init node
        rospy.init_node(node_name, anonymous=True)

        # Register suscriber
        self.sub = rospy.Subscriber("~velocities", WheelsSpeed, self.callback)

        # Init motors
        self.motors = Motors()

    def callback(self, data):
        """Callback on wheels command receiing."""
        self.motors.setWheelsSpeed(data.left, data.right)


if __name__ == "__main__":
    # create the node
    node = MotorNode(node_name="motor")
    # keep spinning
    rospy.spin()
