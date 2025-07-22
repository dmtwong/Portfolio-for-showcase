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
    suits = [card[1] for card in deck_gen]
    ranks = [card[0] for card in deck_gen]
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

# hand_value    
def test_calc_hand_val_1():
    hand_1_c = [('Q', 'Hearts')]
    return bs.calc_hand_val(hand_1_c) == 10

def test_calc_hand_val_2_i():
    hand_2_c_i = [('Q', 'Hearts'), ('A', 'Diamonds')]
    return bs.calc_hand_val(hand_2_c_i) == 21

def test_calc_hand_val_2_ii():
    hand_2_c_ii = [('A', 'Diamonds'), ('K', 'Clubs')]
    return bs.calc_hand_val(hand_2_c_ii) == 21

def test_calc_hand_val_2_iii():
    hand_2_c_iii = [('3', 'Clubs'), ('9', 'Clubs')]
    return bs.calc_hand_val(hand_2_c_iii) == 12

def test_calc_hand_val_2_iv():
    hand_2_c_iv = [('10', 'Hearts'), ('3', 'Diamonds')]
    return bs.calc_hand_val(hand_2_c_iv) == 13

def test_calc_hand_val_5_i():
    hand_5_c_i = [('2', 'Diamonds'), ('2', 'Clubs'), ('2', 'Spades'), 
                  ('3', 'Spades'), ('4', 'Diamonds')]
    return bs.calc_hand_val(hand_5_c_i) == 13

def test_calc_hand_val_5_ii():
    hand_5_c_ii = [('2', 'Diamonds'), ('2', 'Clubs'), ('2', 'Spades'), 
                  ('10', 'Spades'), ('K', 'Diamonds')]
    return bs.calc_hand_val(hand_5_c_ii) == 26

def test_calc_hand_val_5_iii():
    hand_5_c_iii = [('2', 'Diamonds'), ('2', 'Clubs'), ('2', 'Spades'), 
                  ('10', 'Spades'), ('A', 'Diamonds')]
    return bs.calc_hand_val(hand_5_c_iii) == 17

def test_calc_hand_val_5_iv():
    hand_5_c_iv = [('2', 'Clubs'), ('2', 'Clubs'), ('2', 'Spades'), 
                  ('4', 'Spades'), ('A', 'Diamonds')]
    return bs.calc_hand_val(hand_5_c_iv) == 21

def test_calc_hand_val_5_v():
    hand_5_c_v = [('2', 'Clubs'), ('2', 'Clubs'), ('2', 'Spades'), 
                  ('5', 'Spades'), ('A', 'Diamonds')]
    return bs.calc_hand_val(hand_5_c_v) == 12

# hand_w_A_1 = hand_1_c
# def test_calc_hand_val_4(hand_w_A_1): # Ace as 11
#     pass

# hand_w_A_2 = hand_1_c
# def test_calc_hand_val_5(hand_w_A_2): # Ace as 1
#     pass

# simulate_game
# hand_player_1 = hand_1_c
# hand_dealer_1 = hand_1_c


def test_draw_card():
    deck_before = bs.create_deck()
    deck_i = bs.create_deck()
    card_i = bs.draw_card(deck_i)
    # print(card_i)
    try:
        deck_i.index(card_i)
        return False
    except:
        return deck_before.index(card_i)

def test_simulate_hand():
    deck_before = bs.create_deck()  
    deck_i = bs.create_deck()
    hand_i = bs.simulate_hand(deck_i)
    if len(hand_i) < 2:
        return False
    for i in hand_i:
        try:
            deck_i.count(i)
            return False
        except:
            if deck_before.count(i) == 1:
                continue
    return True
    



































