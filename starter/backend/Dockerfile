FROM public.ecr.aws/docker/library/python:3.10-alpine

WORKDIR /app

RUN adduser -u 1000 -D app
RUN apk update && apk add pcre pcre-dev build-base gcc linux-headers openssl libffi-dev && pip install pipenv

COPY Pipfile* ./
RUN pipenv install --system --skip-lock

COPY . .

CMD ["uwsgi", "--http", "0.0.0.0:5000", "--wsgi-file", "app.py", "--callable", "app"]
