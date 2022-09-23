FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /docker/
COPY ./requirements.txt requirements.txt
RUN pip install -r /docker/requirements.txt

COPY ./ src

WORKDIR src/

CMD ["sh", "-c", "python http_server.py"]

