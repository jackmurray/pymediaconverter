FROM python:3

WORKDIR .

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app

ENTRYPOINT [ "python", "/app/pymediaconverter.py" ]
