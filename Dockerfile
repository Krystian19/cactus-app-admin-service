FROM python:3

# ENV vars
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ADMIN_USER="admin"
ENV DJANGO_ADMIN_PASSWORD="pass1234"

RUN apt-get install -y git
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

CMD /code/setup.sh