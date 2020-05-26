# Author Vas Kuruganti

from api import app
from flask import Flask, Response
from flask import make_response
import requests
import os


def test_hello_world():
	
	r = requests.get('http://127.0.0.1:5000')
	assert r.status_code == 200
	assert r.content == b'<p>Hello, World</p>'
	 

def test_hello_world_json():
	assert os.popen('curl localhost:5000 -H "Accept: application/json"').read() == '{"message":"Hello, World"}\n'


def test_app_route():
    x = requests.get('http://127.0.0.1:5000/message')
    assert x.status_code == 200
