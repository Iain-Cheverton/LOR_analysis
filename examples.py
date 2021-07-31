"""Contains examples for later use"""
import json

import requests

from headers import HEADERS

response = requests.get(
    "https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations", headers=HEADERS
)

JSON = json.loads(response.text)

for key, value in JSON.items():
    print(key, value)
