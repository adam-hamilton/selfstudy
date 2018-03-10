#!/usr/bin/python3.6
"""test"""

import json
import requests


def pull(url):
    """test"""
    result = requests.get(url)
    data = json.loads(result.text)
    return data

my_url = 'http://maps.googleapis.com/maps/api/directions/json'
print(pull(my_url))
