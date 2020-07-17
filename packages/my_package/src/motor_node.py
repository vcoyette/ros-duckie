#!/usr/bin/env python

import io
import rospy
from duckietown import DTROS
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float32
from my_package.msg import WheelsSpeed

import picamera
import picamera.array
from my_package.motors import Motors


class MotorNode:
    def __init__(self, node_name):
        rospy.init_node('motor', anonymous=True)
        # construct publisher
        self.sub = rospy.Subscriber("~velocities", WheelsSpeed, self.callback)

        self.motors = Motors()



    def callback(self, data):
        print("ok")
        rospy.loginfo("Receiving {}".format(data))

        self.motors.setWheelsSpeed(data.left, data.right)


if __name__ == "__main__":
    # create the node
    node = MotorNode(node_name="my_node")
    # keep spinning
    rospy.spin()
