FROM python:3.5

RUN apt-get -qq update
RUN apt-get -y install jpegoptim optipng

ADD . /project
WORKDIR /project

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /project/bin/uwsgi.sh
