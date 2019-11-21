FROM ubuntu:18.04

MAINTANER "annmargaret.tutu@icloud.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]