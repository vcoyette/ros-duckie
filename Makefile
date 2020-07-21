.PHONY: run build

CONTAINER_NAME := ros-duckie
VERSION := v1
HOST := mobyduck.local

build:
	docker -H ${HOST} build -t ${CONTAINER_NAME}:${VERSION} .

run:
	docker -H ${HOST} run -it --rm --privileged --net=host ${CONTAINER_NAME}:${VERSION}
