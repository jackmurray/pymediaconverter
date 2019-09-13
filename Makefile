IMAGENAME=pymediaconverter
build:
	sudo docker build -t $(IMAGENAME) .
run:
	sudo docker run --rm -i -t --name="$(IMAGENAME)" $(IMAGENAME)