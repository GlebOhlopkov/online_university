FROM python:3

WORKDIR /online_university

COPY ./requirements.txt /online_university/

RUN pip3 install -r /online_university/requirements.txt

COPY . .
