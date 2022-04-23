FROM python:3 
EXPOSE 8898
RUN useradd tp2022user

RUN apt-get update && apt-get install -y cmake 

COPY . /opt/techprog
WORKDIR /opt/techprog

RUN cmake . && make

RUN pip install --upgrade pip && pip install flask

CMD python3 app.py --port 8898 --host 0.0.0.0

USER tp2022user
