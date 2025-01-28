FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM nginx:latest

RUN mkdir -p /app/staticfiles

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80