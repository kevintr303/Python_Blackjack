suits = {'clubs': '♣', 'diamonds': '♦', 'hearts': '♥', 'spades': '♠'}
values = {"A": [1, 11], "J": 10, "K": 10, "Q": 10}
class Card:
    def __init__(self, rank, suit):
        self.suit = suits[suit]
        self.rank = rank
        try:
            self.value = values[rank]
        except KeyError:
            self.value = int(rank)
        self.visible = True

    def card(self):
        card_spacing = 1 if len(self.rank) == 2 else 2
        return "┌─────┐\n"\
               "|{}  ".format(self.rank) + " " * card_spacing + "|\n"\
               "|  {}  |\n"\
               "|  " .format(self.suit) + " " * card_spacing + "{}|\n"\
               "└─────┘".format(self.rank) \
            if self.visible else \
               "┌─────┐\n"\
               "| /// |\n"\
               "| /// |\n"\
               "| /// |\n"\
               "└─────┘"

    def toggle_visibility(self):
        self.visible = not self.visible
