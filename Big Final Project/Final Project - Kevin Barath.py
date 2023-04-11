# Name: Final Project - Kevin Barath.py
# Author: Kevin Barath
# Date Created: March 13th, 2023
# Date Last Modified: April 10th, 2023

#Purpose:
#
# A casino game with 2 games: rollio and blackjack along with a bar.
# There even is a bar to spend all your hard earned gambling money
# all the money across games and the bar are the same to provide continuity until you are finished
#

import random


# rollio game
def rollio(money):
    
    #
    goal = random.randint(20, 50)
    print(f"The number you need to beat is: {goal}")
    money -= 150
    
    #sputs the user in debt if they are in the -'s
    if money < 0:
        print("Sorry! you are all out of money! You will be forced to pay yout Dues!")
        return money
    
    elif money > 0:
        
        #the rollio game
        rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(5)]
        total = sum(rolls)
        if total > goal:
            print("YOU WON BY LUCK")
            money += 150 * 3.0
            return round(money , 2)
        elif total == goal:
            print("YOU DID NOT WIN OR LOSE")
            money += 150 * 1.7
            return round(money, 2)
        else:
            print("YOU LOST BY LUCK")
            return round(money, 2)

#sfucntion for the black jack game add all the cards up
def sumCards(hand):
    
    # initializes variables
    total = 0
    numAces = 0
    # runs through the cards in the users hand and assigns them a value based of what they are. J, Q, K all = 10, A = 11, everything else is just what the number of the card is
    for card in hand:
        if card[0] in ["J", "Q", "K"]:
            total += 10
        elif card[0] == "A":
            numAces += 1
            total += 11
        else:
            total += int(card[0])
    while total > 21 and numAces > 0:
        total -= 10
        numAces -= 1
    return total

#blackjack game function
def blackJack(money):
    
    money -= 250
    # set up the deck
    deck = []
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
        for rank in range(2, 11):
            deck.append(f"{rank} of {suit}")
        for face in ["Jack", "Queen", "King"]:
            deck.append(f"{face} of {suit}")
        deck.append(f"Ace of {suit}")

    # shuffles the deck
    random.shuffle(deck)

    # deal the cards
    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop()]

    # print the hands
    print(f"\nYour hand: {playerHand}")
    print(f"Dealer's hand: [{dealerHand[0]}, ??]")

    # players turn
    while True:
        ans = input("\nWould you like to hit or stand? (H/S): ")
        if ans.lower() == "h":
            playerHand.append(deck.pop())
            print(f"Your hand: {playerHand}")
            if sumCards(playerHand) > 21:
                print("BUST!")
                return round(money, 2)
        elif ans.lower() == "s":
            break
        else:
            print("Invalid input.")

    # dealer's turn
    while sumCards(dealerHand) < 17:
        dealerHand.append(deck.pop())
        
    print(f"Dealer's hand: {dealerHand}")

    # determine the winner
    playerScore = sumCards(playerHand)
    dealerScore = sumCards(dealerHand)
    
    # multiple if statements for every possible condition
    if playerScore > 21:
        print("Dealer wins!")
        return round(money, 2)
    elif dealerScore > 21:
        print("You win!")
        money += 150 * 2.0
        return round(money, 2)
    elif playerScore > dealerScore:
        print("You win!")
        money += 150 * 2.0
        return round(money, 2)
    elif dealerScore > playerScore:
        print("Dealer wins!")
        return round(money, 2)
    else:
        print("It's a tie!")
        money += 150 * 1.7
        return round(money, 2)

# bar function that adds to the casino 
def bar(money):
    
    # dictionary for all the drinks and their prices
    drinks = {
        "A Great Gig In The Sky": 156000, 
        "Master Of Puppets": 118000, 
        "Whiskey In The Jar": 101000,
        "Ride The Lightning": 87000,
        "The Sanatarium": 67000,
        "Jaded Sunshine": 23000,
        "Casual Wine": 325,
        "Casual Beer": 135,
        "Casual Soda": 100,
              }
    
    # code for the bar to run in a loop
    while True:
        
        ans = input("\nWould you like a drink? (Y/N): ")
        #ifs and elifs for every condition possible from the user
        if ans.lower() == "n":
            break
        elif ans.lower() == "y":
            print("Here are the available drinks and their prices:\n")
            for name, price in drinks.items():
                print(f"{name} - {price}$")
            ans = input("\nWhat would you like to drink? (type 'Leave' to exit): ")
            if ans.lower() == "leave":
                break
            elif ans in drinks:
                price = drinks[ans]
                if money >= price:
                    print(f"You ordered {ans} for {price}$")
                    money -= price
                    return money
                    
                else:
                    print("Sorry, you don't have enough money for that.")
            else:
                print("Sorry, I don't know that drink.")
        else:
            print("Invalid input.")

    print(f"You have {money}$ left.")
    
    
# start menu function
def startMenu():
    
    print("Welcome to Kevin's Kasino!")
    money = 1000
    
    #if's and elifs to see what the user wants to do, it will then call its respective fucntion
    while True:
        print(f"\nYou have {money}$.")
        ans = input("What would you like to do? (1 - Rollio, 2 - Bar, 3 - BlackJack, 4 - Leave): ")
        if ans == "1":
            money = rollio(money)
        elif ans == "2":
            money = bar(money)
        elif ans == "3":
            money = blackJack(money)
        elif ans == "4":
            print("Cya Next Time!")
            break
        else:
            print("Invalid input.")

# start of the program
startMenu()
