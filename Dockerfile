FROM python:3.6

WORKDIR /rpc-microservice 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "nameko run", "rpc_microservice" ]
