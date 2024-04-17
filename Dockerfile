FROM python:3.12.3-alpine
RUN apk update && apk --no-cache add python3-dev libpq-dev bash && mkdir /catalog
WORKDIR /catalog
ADD ./catalog/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt