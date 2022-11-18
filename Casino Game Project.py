#Read Game.txt

import random
import math

dmoney = 100

def rollio(money):

    die1 = [1,2,3,4,5,6]
    die2 = [1,2,3,4,5,6]
    rolls = 0
    rollslimit = 4
    sumofalldies = 0
    goal = random.randint(20,50)

    
    uans0 = input("\n\nWould you like to play Rollio? You have: " + str(money) + " dollars and it costs 25 to play (Y/N):")
    
    if uans0 == "N" or uans0 == "n":
        print ("Goodbye! Comback Later!")
        umoney = money - 0
            
    elif uans0 == "Y" or uans0 == "y":
        umoney = money - 25
            
        uans = input("\nWould you like to know the rules of Rollio? (Y/N): ")

        if uans == "N" or uans == "n":
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

            elif sumofalldies == goal:
                print("\nYOU DID NOT WIN OR LOSE")
            else:
                print("\nYOU LOST BY LUCK")

        elif uans == "Y" or uans == "y":
       
            print("\nRollio (rohl-ee-oh). There are two six sided that are rolled five times per dice.")
            print ("Next, all the rolls are added up and compared to a certain score/goal.")
            print("There is a goal that is randomly generated between 20-50. The max score you can get is 60.")
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
                umoney = money + 100
            elif sumofalldies == goal:
                print("\nYOU DID NOT WIN OR LOSE")
                umoney = money + 25
            else:
                print("\nYOU LOST BY LUCK")

    else:
        print("Invalid Input")
        umoney = money - 0


    print("you now have: " + str(umoney) + " dollars")
    return umoney

    


money = rollio(dmoney)

uans1 = input(str(money) + " Dollars is how much you have left. \nWould you like to play again? (Y/N): ")
while uans1 == "Y" or uans1 == "y":
    rollio(money)

if uans1 == "N" or uans1 == "n":
    print("Bye for now!")
