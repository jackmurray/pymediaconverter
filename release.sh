#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Usage: $0 tagname"
	exit 1
fi

git tag $1
git push --tags
make build
sudo docker tag pymediaconverter:latest jackjcmurray/pymediaconverter:$1
sudo docker push jackjcmurray/pymediaconverter:$1