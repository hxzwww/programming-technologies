FROM python:3

RUN useradd tp2022user

RUN apt-get update && \
    apt-get install -y cmake && \
    apt install -y python3-pip && \
    pip install flask

COPY . /opt/techprog

WORKDIR /opt/techprog 
RUN mkdir build && cd build && cmake .. && make

EXPOSE 8898

USER tp2022user

ENTRYPOINT python3 app.py --port 8898 --host 0.0.0.0
