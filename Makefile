.PHONY: run build

CONTAINER_NAME := ros-duckie
VERSION := v1
# Host on which docker will be ran
HOST := mobyduck.local

build:
	docker -H ${HOST} build -t ${CONTAINER_NAME}:${VERSION} .

run:
	docker -H ${HOST} run -it --rm \
		--privileged \
		--net=host \
		--env ROS_IP=${duckie_ip} \
		-v /opt/vc:/opt/vc \
		${CONTAINER_NAME}:${VERSION}
