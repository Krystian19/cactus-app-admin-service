FROM python:3.7.3-alpine3.9

# ENV vars
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ADMIN_USER="admin"
ENV DJANGO_ADMIN_PASSWORD="pass1234"

RUN apk add --no-cache mariadb-dev build-base

RUN mkdir /code
WORKDIR /code

COPY . /code/
RUN pip install -r requirements.txt

CMD /code/setup.sh