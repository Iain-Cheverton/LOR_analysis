"""This file should be able to access card data and process it to show average outcomes at each mana cost"""
with open("follower_data.txt") as FILE:
    TEXT = FILE.read()
# for line in TEXT.split("	"):
CARDS = TEXT.split("\n")
card_list = [card.split("\t") for card in CARDS]


class Card:
    """temp"""
    def __init__(self, name, mana_cost, power, health):
        self.name = name
        self.mana_cost = mana_cost
        self.power = power
        self.health = health

    def efficiency(self):
        """the total stats divided by the mana_cost"""
        return (self.power + self.health) / self.mana_cost



card_list_2 = [
    Card(*follower[0], int(follower[1]), int(follower[2]), int(follower[3]))
    for follower in card_list
]
for card in card_list_2:
    if card.mana_cost == 1:
        print(card.name)
