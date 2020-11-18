FROM python:3

WORKDIR /usr/src/app

ENV FILE=sensor.csv

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./producer.py" ]