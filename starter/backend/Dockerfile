FROM public.ecr.aws/docker/library/python:3.10-alpine
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

RUN adduser -u 1000 -D app
RUN apk update && \
  apk add \
  pcre \
  pcre-dev \
  build-base \
  gcc \
  linux-headers \
  openssl \
  libffi-dev \
  && pip install pipenv

RUN mkdir -p /var/www/app

COPY Pipfile* ./
RUN pipenv install --system --skip-lock

COPY . .

CMD uwsgi --http :5000 --master --enable-threads -s /var/www/app/app.sock --manage-script-name --mount /=app:app