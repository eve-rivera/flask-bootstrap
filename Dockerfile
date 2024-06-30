FROM python:3.12.4-slim-bullseye

# install psycopg2 dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
    postgresql \
    postgresql-contrib \
    gcc \
    wget \
    ca-certificates \
    libpq-dev

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["bash", "serve.sh"]