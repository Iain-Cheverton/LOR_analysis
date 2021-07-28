"""Contains examples for later use"""
import requests

from api_key import TOKEN

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": str(TOKEN),
}

response = requests.get(
    "https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations", headers=headers
)

print(response.text)
