FROM ros:melodic

RUN apt-get update && apt-get install -y \
    python3-pip \
    python-catkin-tools \
 && rm -rf /var/lib/apt/lists/*

# Create catkin workspace
ENV CATKIN_WS_DIR=/code/catkin_ws
WORKDIR ${CATKIN_WS_DIR}

# Upgrade pip
RUN pip3 install --upgrade pip

# Install cython before installing other dep such as numpy
RUN pip3 install Cython

# install python dependencies
COPY ./dependencies-py.txt .
RUN pip3 install -r dependencies-py.txt

# copy the source code in 
COPY . ./src

# build packages
RUN . /opt/ros/melodic/setup.sh && \
  catkin build

# define command to launch when running
CMD ["bash", "-c", "./src/launch.sh"]

# Usefull for picamera to work
ENV LD_LIBRARY_PATH=/opt/vc/lib

# IP
ENV ROS_IP "192.168.43.99"
ENV ROS_MASTER_URI "http://127.20.10.10:11311/"


