FROM python:latest
RUN pip install -r requirements.txt
WORKDIR /usr/src/app
COPY . .
