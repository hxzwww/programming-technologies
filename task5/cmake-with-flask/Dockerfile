FROM gcc:latest
RUN useradd tp2022user

RUN apt-get update && apt-get install -y cmake 

COPY . /opt/techprog
WORKDIR /opt/techprog

RUN cmake . && make

USER tp2022user


FROM python
RUN useradd tp2022user
EXPOSE 8898

copy . /opt/techprog
WORKDIR /opt/techprog

RUN pip install flask

CMD python3 app.py --port 8898

USER tp2022user
