# Blackjack in Python created by https://github.com/kevintr303 under The MIT License
from card import Card
import random
import sys
from time import sleep

dealer_cards = []
player_cards = []


# The main game
def game_loop():
    dealer_cards.clear()
    player_cards.clear()
    generate_initial_cards()
    print("Dealer:")
    print_cards(dealer_cards)
    print("You:")
    while True:
        print_cards(player_cards)
        total_value, play = ask_for_input()
        if play == "hit":
            hit()
        if play == "stay":
            break
    print("Now it's the dealer's turn..")
    sleep(1)
    print("Revealing Cards")
    dealer_value = reveal_dealer()
    print(f"Dealer got {dealer_value}, and you got {total_value}.")
    if dealer_value > total_value:
        if dealer_value > 21:
            print("Dealer bust! You win!")
            sys.exit()
        print("You lost! Game Over!")
        sys.exit()
    elif dealer_value < total_value:
        print("You won!")
        sys.exit()
    elif dealer_value == total_value:
        print("You tied!")
        sys.exit()


# Generate a random card
def generate_card():
    return Card(random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]),
                random.choice(["clubs", "diamonds", "hearts", "spades"]))


# Check if the random card already exists to prevent duplicates
def check_if_exist(random_card):
    for player_card in player_cards:
        if random_card.rank == player_card.rank and random_card.suit == player_card.suit:
            return True
    for dealer_card in dealer_cards:
        if random_card.rank == dealer_card.rank and random_card.suit == dealer_card.suit:
            return True
    return False


# Generate the intial two cards for both players
def generate_initial_cards():
    while len(dealer_cards) != 2:
        random_card = generate_card()
        if check_if_exist(random_card):
            continue
        dealer_cards.append(random_card)
    dealer_cards[0].toggle_visibility()
    while len(player_cards) != 2:
        random_card = generate_card()
        if check_if_exist(random_card):
            continue
        player_cards.append(random_card)


# Ask for input
def ask_for_input():
    has_an_ace = False
    total_value = 0
    for player_card in player_cards:
        if player_card.rank == "A":
            has_an_ace = True
        else:
            total_value += player_card.value
    if has_an_ace:
        if total_value + 11 > 21:
            total_value += 1
        elif total_value + 11 <= 21:
            total_value += 11
    if total_value == 21 and len(player_cards) == 2:
        print("You got Blackjack. You won!")
        sys.exit()
    if total_value > 21:
        print("You bust! Game Over!")
        sys.exit()
    play = None
    while play not in ["hit", "stay"]:
        play = input(f"You currently have {total_value}. [hit/stay]\n")
    return total_value, play


# Print the cards
def print_cards(card_list):
    print(*[' '.join(x) for x in zip(*[[x.ljust(len(max(s.card().split('\n'), key=len))) for x in s.card().split('\n')] for s in card_list])], sep='\n')


# Hit function
def hit():
    random_card = generate_card()
    while check_if_exist(random_card):
        random_card = generate_card()
    player_cards.append(random_card)


# Reveal the dealer's cards
def reveal_dealer():
    dealer_cards[0].toggle_visibility()
    has_an_ace = False
    total_value = 0
    for dealer_card in dealer_cards:
        if dealer_card.rank == "A":
            has_an_ace = True
        else:
            total_value += dealer_card.value
    added_11 = None
    if has_an_ace:
        if total_value + 11 > 21:
            total_value += 1
        elif total_value + 11 <= 21:
            total_value += 11
            added_11 = True
    while total_value <= 16:
        random_card = generate_card()
        while check_if_exist(random_card):
            random_card = generate_card()
        dealer_cards.append(random_card)
        try:
            total_value += random_card.value
        except TypeError:
            if total_value + 11 > 21:
                total_value += 1
            elif total_value + 11 <= 21:
                total_value += 11
                added_11 = True
        if total_value > 21:
            if has_an_ace and added_11:
                total_value -= 10
                added_11 = False
    for dealer_card in dealer_cards:
        print(dealer_card.card())
        sleep(1)
    return total_value


if __name__ == "__main__":
    print("Welcome to Blackjack! Let's play!")
    game_loop()
