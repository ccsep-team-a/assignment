# A sample Makefile to use make command to build, test and run the program
# Guide: https://philpep.org/blog/a-makefile-for-your-dockerfiles/
APP=isec3004.2020.team-a.assignment

all: build

build:
	docker build --rm --tag=$(APP) .
	docker image prune -f

test:
	docker run -p 0.0.0.0:8000:8000 -it --rm $(APP):latest pytest

run:
	docker run -p 0.0.0.0:8000:8000 -it --rm $(APP):latest

clean:
	docker image rm $(APP)
	docker system prune

.PHONY: all test clean
