.PHONY: run build

CONTAINER_NAME := ros-duckie
VERSION := v1
HOST := mobyduck.local

build:
	docker -H ${HOST} build -t ${CONTAINER_NAME}:${VERSION} .

run:
	docker -H ${HOST} run -it --rm --privileged --net=host -v /opt/vc:/opt/vc ${CONTAINER_NAME}:${VERSION}
