FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y python3 python3-pip nano vim 

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD app.py /

ENTRYPOINT ["python3","app.py"]
