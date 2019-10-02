IMAGENAME=pymediaconverter
build:
	sudo docker build -t $(IMAGENAME) .
	sudo docker build -t $(IMAGENAME)-audioworker . -f Dockerfile.audioworker
run:
	sudo docker run -v /tmp/docker:/data --rm -i -t --name="$(IMAGENAME)" $(IMAGENAME) --loglevel DEBUG
