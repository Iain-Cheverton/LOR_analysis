"""This file should be able to access card data and process it to show average outcomes at each mana cost"""
import statistics as stats

import matplotlib.pyplot as plt  # pylint: disable=import-error

with open("follower_data.txt") as FILE:
    TEXT = FILE.read()
CARDS = TEXT.split("\n")
card_list = [card.split("\t") for card in CARDS]


class Card:
    """
    A class used to represent a card
     Attributes
    ----------
    name : str
        the name of the Card
    mana_cost : int
        the mana required to play the card
    power : int
        the attack power of the card
    health : int
        the amount of damage the card can take before being destroyed
    """

    def __init__(self, name, mana_cost, power, health):
        self.name = name
        self.mana_cost = int(mana_cost)
        self.power = int(power)
        self.health = int(health)

    def stat_total(self):
        """The total stats for a card"""
        return self.power + self.health

    def efficiency(self):
        """the total stats divided by the mana_cost"""
        return (self.power + self.health) / (self.mana_cost + 1)


CARD_LIST = [Card(*follower) for follower in card_list]


def average_result():
    """Creates a dictionary of the average stat outcome for each possible mana cost of tri-beam"""
    return {mana_cost: average(mana_cost) for mana_cost in range(1, 11)}


def average(mana_cost):
    """Finds the average stat value for a specific mana cost of follower"""
    cards = [card for card in CARD_LIST if card.mana_cost == mana_cost]
    return stats.mean(card.power for card in cards), stats.mean(
        card.health for card in cards
    )


fig, ax = plt.subplots()
ax.plot(average_result().keys(), [sum(y) for y in average_result().values()])
ax.plot(average_result().keys(), average_result().values())
plt.title("The Average Tri-beam Follower Stats For Each Possible Mana-Cost")

plt.show()
