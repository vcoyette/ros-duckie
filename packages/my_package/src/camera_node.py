#!/usr/bin/env python

import io
import rospy
from duckietown import DTROS
from sensor_msgs.msg import CompressedImage

import picamera
import picamera.array


# https://picamera.readthedocs.io/en/release-1.13/recipes2.html#rapid-capture-and-streaming
class CameraPublisherNode(DTROS):
    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(CameraPublisherNode, self).__init__(node_name=node_name)
        # construct publisher
        self.pub = rospy.Publisher("~image/compressed", CompressedImage, queue_size=1)
        self.camera = picamera.PiCamera(resolution='VGA', framerate=30)
        self.camera.framerate = 30
        self.camera.exposure_mode = "sports"
        self.stream = io.BytesIO()

    def run(self):
        output = SplitFrames(self.pub)
        self.camera.start_recording(self, format='mjpeg')

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # Start of new frame; send the old one's length
            # then the data
            size = self.stream.tell()
            if size > 0:
                self.stream.seek(0)
                message = CompressedImage()
                message.header.stamp = rospy.Time.now()
                message.data = self.stream.read(size)
                self.pub.publish(message)
                print("Publishing")
                self.stream.seek(0)
        self.stream.write(buf)



if __name__ == "__main__":
    # create the node
    node = CameraPublisherNode(node_name="my_node")
    # run node
    node.run()
    # keep spinning
    rospy.spin()
