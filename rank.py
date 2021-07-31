"""Contains command relating to the masters leaderboard for Legends of Runeterra"""
import json

import requests

from headers import HEADERS


def rank(username: str, region: str):
    """attempts to find the rank and LP of a given player"""
    response = requests.get(
        f"https://{region}.api.riotgames.com/lor/ranked/v1/leaderboards",
        headers=HEADERS,
    )
    leaderboard = json.loads(response.text)
    for player in leaderboard["players"]:
        if player["name"].lower() == username.lower():
            return f"{player['name']} is rank {player['rank'] + 1} and their LP is {player['lp']}"
    return f"{username} is not in master"


def get_rank(rank_number: int, region: str):
    """returns the player and LP for a given rank"""
    response = requests.get(
        f"https://{region}.api.riotgames.com/lor/ranked/v1/leaderboards",
        headers=HEADERS,
    )
    leaderboard = json.loads(response.text)
    player = leaderboard["players"][rank_number - 1]
    return f"{player['name']} is rank {rank_number} and their LP is {player['lp']}"


print(rank("alanzq", "europe"))
print(get_rank(1, "americas"))
