FROM ubuntu:18.04

MAINTANER Noi Nguyen "huunoidq@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# Install all required libs
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "challege_b.py" ]