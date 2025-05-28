FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh


CMD ["./run.sh"]  
#docker, docker compose, dockerfile yêu cầu lưu (ctrl s) thì code trong docker sẽ tự thay đởi và update