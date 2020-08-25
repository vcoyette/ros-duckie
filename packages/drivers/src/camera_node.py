#!/usr/bin/env python3
"""Camera Publisher."""

import io
import rospy
from sensor_msgs.msg import CompressedImage

import picamera
import picamera.array


class CameraPublisherNode(object):
    """Camera Node.

    Publishes images to ~velocities.
    """

    def __init__(self, node_name):
        """Initialise Camera node.

        Args:
            node_name: Default name of the node.
        """
        # Init node
        rospy.init_node(node_name, anonymous=True)

        # Register publisher
        self.pub = rospy.Publisher("~image/compressed", CompressedImage, queue_size=1)

        # Init camera
        self.camera = picamera.PiCamera(resolution="VGA", framerate=15)

        # The simulator has a framerate of 30 and skip 1 frame per timestep
        self.camera.framerate = 15
        self.camera.exposure_mode = "sports"

        # Stream to build msg to publish
        self.stream = io.BytesIO()

    def run(self):
        """Run the node"""
        # Start recording, using self as output to trigger the write method
        # on each frame
        self.camera.start_recording(self, format="mjpeg")

    # See https://picamera.readthedocs.io/en/release-1.13/recipes2.html#rapid-capture-and-streaming
    def write(self, buf):
        """Publish current stream and write current buffer to stream."""
        if buf.startswith(b"\xff\xd8"):
            # Start of new frame; send the old one's length
            # then the data
            size = self.stream.tell()
            if size > 0:
                self.stream.seek(0)
                message = CompressedImage()
                message.header.stamp = rospy.Time.now()
                message.data = self.stream.read(size)
                self.pub.publish(message)
                self.stream.seek(0)
        self.stream.write(buf)


if __name__ == "__main__":
    # create the node
    node = CameraPublisherNode(node_name="camera")
    # run node
    node.run()
    # keep spinning
    rospy.spin()
