FROM python:3.11

WORKDIR /data

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4200

CMD python3 run.py 0.0.0.0:4200