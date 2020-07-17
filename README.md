# ROS Duckie

Usage:

1. Build the docker image using:
```bash
docker -H mobyduck.local build -t ros-duckie:v1 .
```

2. Run it using:
```bash
docker -H mobyduck.local run -it --rm --privileged --net=host ros-duckie:v1
```
