# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:39:48 2025

@author: mingt
"""

""" Intend to write a python application that simulates a multiplayer game;
will start with single-player game against a dealer and supports basic game rule 
including hit, stand, blackjack rules, dealer rules
"""

"""
Create a deck:
    # INPUT: None
    # OUTPUT: An array of 52 cards (4 suits, 13 cards each)
"""

# import sys
# import os
# m_path = os.path.abspath(os.path.join(os.path.dirname(__path__), '..', 'blackjeck_simulator'))
# sys.path.append(m_path)

def create_deck():
    ranks = list(map(str, range(2,11)))
    ranks.extend(['J','Q','K', 'A'])    
    suits = ["Spades" , "Hearts" , "Clubs" , "Diamonds"]
    deck_i = [(r, s) for s in suits for r in ranks] 
    return deck_i[:]

"""
Calculate hand value:
    # INPUT: An array of x cards (from 1 to x - 1 as long as sum before draw is less than 21 or 5 for some variant) 
    # OUTPUT: Calculate hand value given input
"""
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,    '6': 6, '7': 7, '8': 8, '9': 9, 
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def calc_hand_val(hand):
    total = sum(card_values[card[0]] for card in hand)
    aces = hand.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


"""
draw a card:
"""
def simulate_hand(remain_deck):
    pass    

"""
Generate a hand:
"""
def simulate_hand(remain_deck):
    pass    



"""
Simulate a game
    # INPUT: an array that contain cards that are not drawn
    # OUTPUT: return Win, draw, loss 
"""
def simulate_game(remain_deck):
    pass





























