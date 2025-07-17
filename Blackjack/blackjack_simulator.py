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
    deck_i = [(s, r) for s in suits for r in ranks] 
    return deck_i[:]

"""
Calculate hand value:
    # INPUT: An array of x cards (from 1 to x - 1 as long as sum before draw is less than 21 or 5 for some variant) 
    # OUTPUT: Calculate hand value given input
"""
def calc_hand_val(hand):
    pass

"""
Simulate a game
    # INPUT: An array of x and y cards (x for player, y for dealer)
    # OUTPUT: return Win, draw, loss 
"""
def simulate_game(hand_player, hand_dealer):
    pass

