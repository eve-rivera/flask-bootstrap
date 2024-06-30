FROM python:3.12.4-slim-bullseye

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["bash", "serve.sh"]