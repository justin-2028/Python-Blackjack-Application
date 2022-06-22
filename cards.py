#! /usr/bin/env python3

import random


def get_deck():
    deck = []
    ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King"}
    suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = 11
            elif rank == "Jack" or rank == "Queen" or rank == "King":
                value = 10
            else:
                value = int(rank)

            card = [rank, suit, value]
            deck.append(card)
    return deck


def shuffle(deck):
    random.shuffle(deck)


def deal_card(deck):
    card = deck.pop()
    return card


def get_empty_hand():
    hand = []
    return hand


def add_card(hand, card):
    hand.append(card)


def get_points(hand):
    points = 0
    ace_count = 0
    for card in hand:
        if card[0] == "Ace":
            ace_count += 1
        points += card[2]

    if ace_count > 0 and points > 21:
        points = points - (ace_count * 10)
    if ace_count > 1 and points <= 11:
        points += 10
    return points


def main():
    deck = get_deck()
    shuffle(deck)
    for card in deck:
        print(card)
    print()

    hand = get_empty_hand()
    add_card(hand, deal_card(deck))
    add_card(hand, deal_card(deck))
    add_card(hand, deal_card(deck))

    print("Hand:", hand)
    print("Points:", get_points(hand))


if __name__ == "__main__":
    main()
