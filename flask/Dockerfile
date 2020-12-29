FROM ubuntu:20.04

WORKDIR /app


RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    build-essential libssl-dev libffi-dev python3-setuptools \
    python3-venv mongodb-clients

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY ./flask/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000
#COPY . .

# CMD tail -f /dev/null
CMD [ "python3", "app.py" ]