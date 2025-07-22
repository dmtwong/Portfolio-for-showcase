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

import random
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
def draw_card(deck_current):
    draw_i = random.choice(range(len(deck_current)))
    return deck_current.pop(draw_i)


"""
Generate a hand:
"""
def simulate_hand(deck_current): #, isDealer = True) # hand_current):
    # if isDealer and len(hand_current) == 1:  # dealer show first card
        # pass
    handcurrent = []
    handcurrent.append(draw_card(deck_current))
    handcurrent.append(draw_card(deck_current))
    # print(handcurrent, len(deck_current))
    while calc_hand_val(handcurrent) < 17:
        handcurrent.append(draw_card(deck_current))
    # print(handcurrent, len(deck_current))
    return handcurrent    

"""
Simulate a game
    # INPUT: an array that contain cards that are not drawn
    # OUTPUT: return Win, draw, loss 
"""
def simulate_game(remain_deck):
    dealer_hand = simulate_hand(remain_deck)
    player_hand = simulate_hand(remain_deck)
    print(dealer_hand)
    player_value = calc_hand_val(player_hand)
    print(player_hand, player_value)
    if player_value > 21:
        return -1 # loss if player's hand exceed 21
    dealer_value = calc_hand_val(dealer_hand)
    print(dealer_value)
    if dealer_value > 21 or player_value > dealer_value:
        return 1 # player win
    elif player_value == dealer_value:
        return 0 # draw if hands tie
    else:
        return -1 # player loss
    
# # random.choice(range(10))
deck_0 = create_deck()
# deck_i = create_deck()
# card_i = draw_card(deck_i)
# card_i
# # len(deck_i)
# # deck_i.index(card_i)
# # deck_0.index(card_i)
# hand_i = simulate_hand(deck_i)
# for i in hand_i:
#     print(i)
#     # try:
#     #     deck_i.index(hand_i[i])
#     #     False
#     # except:
#     print(deck_0.count(i))

simulate_game(deck_0)

    


















