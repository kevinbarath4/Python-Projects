import tkinter as tk
import random
from PIL import Image, ImageTk

# Global constants for card ranks and suits
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'S', 'D', 'C']

def deal_cards():
    """Deals two cards to the player and the dealer."""
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(random.choice(RANKS) + random.choice(SUITS))
        dealer_hand.append(random.choice(RANKS) + random.choice(SUITS))
    return player_hand, dealer_hand

def get_score(hand):
    """Calculates the score of a blackjack hand."""
    score = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            num_aces += 1
        else:
            score += int(rank)
    # If the score is over 21, set as many aces as possible to value 1
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

def player_turn(player_hand, dealer_hand, hit_button, stand_button):
    """Takes the player's turn by allowing them to hit or stand."""
    def hit():
        """Hits the player and checks if they have bust."""
        player_hand.append(random.choice(RANKS) + random.choice(SUITS))
        update_hands()
        if get_score(player_hand) > 21:
            end_game('You bust!')
    def stand():
        """Ends the player's turn and starts the dealer's turn."""
        hit_button.pack_forget()
        stand_button.pack_forget()
        dealer_turn(dealer_hand, player_hand)
    hit_button['command'] = hit
    stand_button['command'] = stand

def dealer_turn(dealer_hand, player_hand):
    """Takes the dealer's turn by hitting until the score is at least 17."""
    while get_score(dealer_hand) < 17:
        dealer_hand.append(random.choice(RANKS) + random.choice(SUITS))
        update_hands()
    determine_winner(player_hand, dealer_hand)

def determine_winner(player_hand, dealer_hand):
    """Determines the winner of the game based on the scores of the player and dealer."""
    player_score = get_score(player_hand)
    dealer_score = get_score(dealer_hand)
    if player_score > 21:
        end
