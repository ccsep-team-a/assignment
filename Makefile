APP=isec3004.2020.team-a.assignment

all: build test run 

build:
	docker build --rm --tag=$(APP) .
	docker image prune -f

test: build
	docker run -p 0.0.0.0:8000:8000 -it --rm $(APP):latest pytest -v 

run:
	docker run -p 0.0.0.0:8000:8000 -it --rm $(APP):latest

clean:
	docker image rm $(APP)
	docker system prune
