FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENV DOCKER=1


ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]