# ROS Duckie

This repository contains the code to build a docker image to run on the duckiebot (https://www.duckietown.org/).

This image contains the configuration of a ROS master runing two nodes:
* CameraNode: Node which publishes images from the camera,
* MotorNode: Node which subscribes to a wheel speed command topic, and controlling the motors. 

Usage:

1. Build the docker image using:
```bash
make build
```

2. Run it using:
```bash
make run
```

