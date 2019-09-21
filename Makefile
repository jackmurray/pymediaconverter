IMAGENAME=pymediaconverter
build:
	sudo docker build -t $(IMAGENAME) .
run:
	sudo docker run -v /tmp/docker:/data --rm -i -t --name="$(IMAGENAME)" $(IMAGENAME)
