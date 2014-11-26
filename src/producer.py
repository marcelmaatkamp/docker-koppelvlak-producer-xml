#!/usr/bin/env python

from kombu import Connection, Exchange, Queue
from kombu import Producer
from kombu.common import maybe_declare
from kombu.pools import producers
from socket import *
import time
import re
import json
import os
import io

exchangeName = "orca.export"
topdir = '/koppelvlak/orcaexports/'
exten = '.xml'

exchange = Exchange(exchangeName, type="fanout")

with Connection('amqp://guest:guest@rabbitmq:5672//') as connection:
  channel = connection.channel()
  with Producer(channel, exchange = exchange, serializer="json") as producer:
    while True:
      for dirpath, dirnames, files in os.walk(topdir):
        path = dirpath.split('/')
        for name in files:
          if name.lower().endswith(exten):
            filename = os.path.join(dirpath, name)
            print len(path)*'-', filename
            file = io.open( filename, "r", encoding="iso-8859-1" )
            data = file.read()[2:]
            headers = {"path": dirpath, "name": name}
            producer.publish(
              data,
              headers=headers,
              exchange=exchange,
              routing_key='orca',
              content_type="application/xml",
              content_encoding="binary",
            )
            os.remove(filename)
