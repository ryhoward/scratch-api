FROM ubuntu:20.04

RUN apt update -y && \
    apt install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN echo $(python3 --version)

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

#ENTRYPOINT ["echo", "Hello World!"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
