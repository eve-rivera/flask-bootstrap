FROM python:3.12.4-slim-bullseye

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y \
    postgresql \
    postgresql-contrib \
    gcc \
    wget \
    curl \
    ca-certificates \
    libpq-dev

RUN curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install -y nodejs

RUN npm install -g -D @playwright/test
RUN npx playwright install --with-deps

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["bash", "bin/serve.sh"]