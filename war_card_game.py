'''
    Ronan Ballantine
    WAR card game
    22/02/2022
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
          'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.lower()]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.full_deck = []

        # Creates full deck
        for suit in suits:
            for rank in ranks:
                self.full_deck.append(Card(suit, rank))

    def shuffle(self):
        # Shuffles Deck
        random.shuffle(self.full_deck)

    def deal_one(self):
        # Takes card from the deck
        return self.full_deck.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.player_cards = []

    # Removes card from players hand
    def play_card(self):
        card = self.player_cards.pop(0)
        print(f"Player {self.name}'s card is {card}")

        return card

    # Adds cards to players hand
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)
        else:
            self.player_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards.'


player_one = Player('One')
player_two = Player('Two')

# Create a new deck and shuffle it
new_deck = Deck()
new_deck.shuffle()


# Distribute cards among the two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# Start the game
game_on = True

game_round = 0
while game_on:

    game_round += 1
    print(f"Round {game_round}")

    # Check if player one has cards remaining
    if len(player_one.player_cards) == 0:
        print("\nPlayer Two Wins!")
        game_on = False
        break

    # Checks if player two has cards remaining
    if len(player_two.player_cards) == 0:
        print("\nPlayer One Wins!")
        game_on = False
        break

    # Starts new round
    player_one_cards = []
    player_one_cards.append(player_one.play_card())

    player_two_cards = []
    player_two_cards.append(player_two.play_card())

    at_war = True

    while at_war:

        # If player One's card is greater
        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            print(f"Player {player_one.name} gets the cards")
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print(player_one)
            print(player_two)

            at_war = False

        # Player Two's card is greater
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            print(f"Player {player_two.name} gets the cards")
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print(player_one)
            print(player_two)

            at_war = False

        else:
            print('WAR!')

            # Check if the players have 5 cards remaining
            if len(player_one.player_cards) < 5:
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.player_cards) < 5:
                print("Player One Wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.play_card())
                    player_two_cards.append(player_two.play_card())
