#!/usr/bin/env python
from urllib2 import Request, urlopen
import json, sys
import requests

HELLO_WORLD_SERVICE = {
  "name": "hello-world2",
  "memory": 100,
  "ports": [80],
  "instances": 2,
  "image": "tutum/hello-world",
  "environment": [{"key": "PORT", "value": "80"}],
  "version": "hello1",
  "enabled": True,
  "cpu": 0.1
}

HELLO_WORLD_LB = {
  "name": "hello-world2",
  "enabled": True,
  "hostname": "hello.example.fi",
  "service_id": None, # get this from Halti
  "source_port": 80, # which port (inside the container) should be served by Luotsi/LB
  "force_https": False,
  "ports": {
    "http": True,
    "https": False
  },
}

if len(sys.argv) < 2:
    print('Usage: hello_world.py http://halti-master:4040')
    sys.exit(-1)

HALTI_URL = sys.argv[1]

r = requests.post('{}/api/v1/services'.format(HALTI_URL), json=HELLO_WORLD_SERVICE)
print(r.text)
service = r.json().get('service', {}).get('service_id')
if not service:
    print('SERVICE_NONE')
    sys.exit(-1)

HELLO_WORLD_LB['service_id'] = service
r = requests.post('{}/api/v1/loadbalancers'.format(HALTI_URL), json=HELLO_WORLD_LB)
print(r.text)
print('services configured')
sys.exit(0)