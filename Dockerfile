# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY Weather_App-0.1.1.tar.gz Weather_App-0.1.1.tar.gz
RUN pip install Weather_App-0.1.1.tar.gz
RUN rm /app/Weather_App-0.1.1.tar.gz

EXPOSE 8080

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]