FROM python:latest
COPY . .
RUN pip install -r requirements.txt
WORKDIR /usr/src/app

