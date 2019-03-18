FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y install python3 python3-pip

WORKDIR /home/test-task

COPY server .

RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD ["python3", "main.py"]