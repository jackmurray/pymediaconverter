FROM python:3

RUN apt update && apt-get -y install ffmpeg && rm -rf /var/cache/apt

WORKDIR .

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app

ENTRYPOINT [ "python", "/app/pymediaconverter.py" ]
