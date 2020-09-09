# ROS Duckie

This repository contains the code to build a docker image to run on the duckiebot (https://www.duckietown.org/).

This image contains the configuration of a ROS master runing two nodes:
* CameraNode: Node which publishes images from the camera,
* MotorNode: Node which subscribes to a wheel speed command topic, and controlling the motors. 

## Requirements
This app requires docker to be built and ran.

It also requires to know the ip of the duckie.
To find it, you can run:
```bash
ping mobyduck.local
```
(replace mopbyduck with the hostname of your duckie).

Store this ip, we will refer to it as ROS_IP later.


Usage:

1. Build the docker image using:
```bash
make build
```

2. Run it using:
```bash
make run duckie_ip=ROS_IP
```
replace ROS_IP with the

