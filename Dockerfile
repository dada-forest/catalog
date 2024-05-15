FROM python:latest
RUN apt-get update -y
WORKDIR /catalog
ADD requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir