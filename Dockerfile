FROM dockerfile/python 
RUN pip install librabbitmq kombu 

RUN mkdir /src
WORKDIR /src
COPY src /src

CMD ["python", "producer.py"]
