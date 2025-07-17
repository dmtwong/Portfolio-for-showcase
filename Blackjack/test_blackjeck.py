# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 18:51:43 2025

@author: mingt
"""


import pytest
import sys
# import os

# from pathlib import Path
# print(Path.cwd())
# print(Path(__file__).resolve())
# os.listdir()
# print(sorted(os.listdir('.')))

# file_path = os.path.realpath("")
# file_path
# os.path.dirname("test_blackeck.py")
# os.path.dirname(__file__)

# pathlib.Path("blackjeck_simulator.py").cwd()
# pathlib.Path(__file__).parent.resolve()

# print(os.getcwd())
# os.chdir('C:\\Users\\mingt\\Downloads\\Portfolio-for-showcase\\Blackjack')
sys.path.append('C:\\Users\\mingt\\Downloads\\Portfolio-for-showcase\\Blackjack')
# os.getcwd()
import blackjack_simulator as bs

# create_deck
def test_create_deck():
    # deck_gen = create_deck()   
    deck_gen = bs.create_deck() 
    # n_cards = len(deck_gen)
    # is_Full = n_cards % 52 == 0
    if len(set(deck_gen)) % 52 != 0:
        return False
    suits = [card[0] for card in deck_gen]
    ranks = [card[1] for card in deck_gen]
    suits.sort()
    ranks.sort()
    unique_ranks = list(dict.fromkeys(ranks))
    unique_suits = list(dict.fromkeys(suits))
    for i in unique_suits:
        if ranks.count(i) % 13 != 0:
            return False
    for i in unique_ranks:
        if ranks.count(i) % 4 != 0:
            return False
    return True

# # hand_value    
# hand_1_c = ['Q']
# def test_calc_hand_val_1(hand_1_c):
#     pass

# hand_2_c = hand_1_c
# def test_calc_hand_val_2(hand_2_c):
#     pass

# hand_5_c = hand_1_c
# def test_calc_hand_val_3(hand_5_c):
#     pass

# hand_w_A_1 = hand_1_c
# def test_calc_hand_val_4(hand_w_A_1): # Ace as 11
#     pass

# hand_w_A_2 = hand_1_c
# def test_calc_hand_val_5(hand_w_A_2): # Ace as 1
#     pass

# # simulate_game
# hand_player_1 = hand_1_c
# hand_dealer_1 = hand_1_c
# def test_simulate_game(hand_player_1, hand_dealer_1):
#     pass
