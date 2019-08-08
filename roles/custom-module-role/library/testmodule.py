#!/bin/env python
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
  "first": {"required": True, "type": "int"},
  "second": {"required": True, "type": "int"}
  }
  module = AnsibleModule(argument_spec=fields)
  # yourName = os.path.expanduser(module.params['yourName'])
  # newName = firstProg(yourName)
  newName = module.params['first'] + module.params['second']
  # + os.path.expanduser(module.params['second'])
  module.exit_json(msg=newName)
