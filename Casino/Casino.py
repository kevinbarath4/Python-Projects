#Read Game.txt

import random
import math
import sys 


def rollioExp(money2):

    die1 = (1,2,3,4,5,6)
    die2 = (1,2,3,4,5,6)
    rolls = 0
    rollslimit = 4
    sumofalldies = 0
    goal = random.randint(20,50)

    print("\nAlright then Expert, its all you!")
    print("\nThe number you need to beat is: " + str(goal))

    while rolls <= rollslimit:
        random_num0 = random.choice(die1)
        random_num1 = random.choice(die2)
        print("The rolls you got were: " + str(random_num0) + " and " + str(random_num1))
        totaldie = random_num0 + random_num1
        sumofalldies += totaldie
        print("Sum of roll: " + str(totaldie))
        rolls += 1

    print("Sum of all roles: " + str(sumofalldies))
    print("You needed to get: " + str(goal))

    if sumofalldies > goal:
        print("\nYOU WON BY LUCK")
        money2 = money2 * 2.2
    elif sumofalldies == goal:
        print("\nYOU DID NOT WIN OR LOSE")
        money2 = money2 *  1.5
    else:
        print("\nYOU LOST BY LUCK")
    
    return money2

def rollioInExp(money3):

    die1 = (1,2,3,4,5,6)
    die2 = (1,2,3,4,5,6)
    rolls = 0
    rollslimit = 4
    sumofalldies = 0
    goal = random.randint(20,50)

    print("\nRollio (rohl-ee-oh). There are two six sided that are rolled five times per dice.")
    print ("Next, all the rolls are added up and compared to a certain score/goal.")
    print("There is a goal which you need to beat that is randomly generated between 20-50. The max roll score you can get is 60.")
    print("HAVE FUN")
        
    print("\nThe number you need to beat is: " + str(goal))

    while rolls <= rollslimit:
        random_num0 = random.choice(die1)
        random_num1 = random.choice(die2)
        print("The rolls you got were: " + str(random_num0) + " and " + str(random_num1))
        totaldie = random_num0 + random_num1
        sumofalldies += totaldie
        print("Sum of roll: " + str(totaldie))
        rolls += 1

    print("Sum of all roles: " + str(sumofalldies))
    print("You needed to get: " + str(goal))

    if sumofalldies > goal:
        print("\nYOU WON BY LUCK")
        money3 = money3 * 1.4
    elif sumofalldies == goal:
        print("\nYOU DID NOT WIN OR LOSE")
        money3 = money3 + 25
    else:
        print("\nYOU LOST BY LUCK")
    
    return money3

def rollio(money):

    die1 = (1,2,3,4,5,6)
    die2 = (1,2,3,4,5,6)
    rolls = 0
    rollslimit = 4
    sumofalldies = 0
    goal = random.randint(20,50)
    rollio = True

    while rollio == True:

        uans0 = input("\nAre you ready to roll? (Y/N): ")
    
    
        if uans0 == "N" or uans0 == "n":
            amoney = money
            print ("\nGoodbye! Comback Later! You have: " + str(amoney) + "$")  
            return amoney

        elif uans0 == "Y" or uans0 == "y":
            amoney = money - 25

            uans = input("Would you like to know the rules of Rollio? (Y/N): ")

            if uans == "N" or uans == "n":
                tmoney = rollioExp(amoney)
                print("you now have: " + str(tmoney) + "$\n")
                return tmoney
            elif uans == "Y" or uans == "y":
                tmoney = rollioInExp(amoney) 
                print("you now have: " + str(tmoney) + "$\n")
                return tmoney
            
        else:
            print("Invalid Input")
            amoney = money 
            print("you now have: " + str(amoney) + "$\n")
            

def bar(money4):

    bararea = True
    
    while bararea == True:
        uans3 = input("\nHey There! Would you like a drink? (Y/N): ")

        if uans3 == "Y" or "y":

            while bararea == True and uans3 == "Y" or uans3 == "y":

                uans4 = input("\nWhat would would like to drink? You have: " + str(money4) + "$. If you would like to leave, type 'Leave'. \n1 - Taste of Diamonds (20,700$) \n2 - Shipwrecked Champagne (14,181$) \n3 - 1928 Krug (12,851$) \n4 - Veuve Clicot (7,543$) \n5 - Dom Perignon (5,123$) \n: ")

                if uans4 == "1" and money4 >= 20700:
                    print("Enjoy the Taste of Diamonds high roller!")
                    money4 =- 20700
                elif uans4 == "1" and money4 != 20700:
                    print("You dont have that money yet!")
                elif uans4 == "2" and money4 >= 14181:    
                    print("Enjoy the Shipwrecked Champagne Captain!")
                    money4 =- 14181
                elif uans4 == "2" and money4 != 14181:
                    print("You dont have that money yet!")  
                elif uans4 == "3" and money4 >= 12851:
                    print("Enjoy the 1928 Krug like the good ol' times")
                    money4 =- 12851
                elif uans4 == "3" and money4 != 12851:
                    print("You dont have that money yet!")
                elif uans4 == "4" and money4 >= 7543:
                    print("Enjoy the Veuve Clicot!")
                    money4 =- 7543
                elif uans4 == "4" and money4 != 7543:
                    print("You dont have that money yet!")
                elif uans4 == "5" and money4 >= 5123:
                    print("Enjoy the Dom Perignon")
                    money4 =- 5123
                elif uans4 == "5" and money4 != 5123:
                    print("You dont have that money yet!")
                elif uans4 == "Leave" or uans4 == "leave":
                    print("Hope to see you back here!")
                    break
                else:
                    print("Invalid Input")

    
        elif uans3 == "N" or uans3 == "n":
            print("Hope to see you back here!")
            break
        
        else:
            print("Invalid Input")
        
        break
    

    return money4       


def startmenu():

    dmoney = 100
    start = True
    
    while start == True:

        uans1 = input("\nWould you like to play in the Casino or go into the Bar? \n\n1 - Casino \n2 - Bar \n: ")

        if uans1 == "1":
            while uans1 == "1":

                print("\nYour Balance is: " + str(dmoney) + "$")
                uans2 = input("\nType the number of the game you would like to play! \nType 'Leave' if you would like to leave the casino.  \n\n1 - Rollio \n: ")
        
        
                if uans2 == "1":
                    dmoney = rollio(dmoney)

                elif uans2 == "Leave" or uans2 == "leave":
                    print("Thanks for joining in the Casino! You ended with a balance of: " + str(dmoney) + "$")
                    break

                elif uans2 != "Leave" or uans2 != "leave":
                    print("Invalid input")
                
        

        elif uans1 == "2":
            print("\nSure, the bar is that way!")
            dmoney = bar(dmoney)

        elif uans1 != "1" or uans2 != "2":
            print("Invalid Input\n")
    

startmenu()


        

