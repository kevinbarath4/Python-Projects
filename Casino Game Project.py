#Read Game.txt

import random
import math



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
        money2 = money2 + 100
    elif sumofalldies == goal:
        print("\nYOU DID NOT WIN OR LOSE")
        money2 = money2 + 25
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
        money3 = money3 + 100
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
        return amoney

   

def startmenu():

    dmoney = 100

    uans1 = input("Would you like to play in the casino? (Y/N): ")

    while uans1 == "Y" or uans1 == "y":

        print("\nYour Balance is: " + str(dmoney) + "$")
        uans2 = input("Type 'Leave' if you would like to leave the casino. If you would like to play, what game? (Type name of game)  \n\n-Rollio \n: ")
        
        
        if uans2 == "rollio" or uans2 == "Rollio":
            dmoney = rollio(dmoney)

        elif uans2 == "Leave" or uans2 == "leave":
            print("Thanks for playing, you ended with a balance of: " + str(dmoney) + "$")
            break

        else:
            print("Invalid input")
            
        

    if uans1 == "N" or uans1 == "n":
        print("Sure, the bar is that way!")
    

startmenu()


        

