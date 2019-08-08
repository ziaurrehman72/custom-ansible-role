#!/bin/env python
from time import sleep
from json import dumps
from kafka import KafkaProducer
from ansible.module_utils.basic import *
# import KafkaConsumer
import os, json
import re, sys

# import kafka
def firstProg(text):
  text1 = "Hello " + text
  return text1
if __name__ == '__main__':
  fields = {
  "data": {"required": True, "type": "str"},
  "topic": {"required":True, "type": "str"},
  "hostname": {"required":True, "type": "str"}
  }
  module = AnsibleModule(argument_spec=fields)
  producer = KafkaProducer(bootstrap_servers=['192.168.1.115:9092'],
                           value_serializer=lambda x:
                           dumps(x).encode('utf-8'))
  # yourName = os.path.expanduser(module.params['yourName'])
  # newName = firstProg(yourName)
  # newName = module.params['first'] - module.params['second']
  producer.send(module.params['topic'], value=module.params['data'])
  # + os.path.expanduser(module.params['second'])
  module.exit_json(msg=module.params['data'])
