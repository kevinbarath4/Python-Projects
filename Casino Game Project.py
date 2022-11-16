#Read Game.txt

import random
import math


die1 = [1,2,3,4,5,6]
die2 = [1,2,3,4,5,6]
rolls = 0
rollslimit = 4
sumofalldies = 0
goal = random.randint(20,50)
money = 100

ans = input("Would you like to play Rollio? (Y/N): ")

if ans == "N" or "n":
    print("Bye! Come Back Later!!")
    
else:
    input("Would you like to know the rules of Rollio? (Y/N): ")

    if ans == "Y" or "y":
        print("Rollio (rohl-ee-oh). There are two six sided that are rolled five times per dice. \nNext, all the rolls are added up and compared to a certain score/goal. \nThe goal is randomly generated number from 20-50 to make it somewhat easy. \nHAVE FUN")
    else:
        print("\nThe number you need to beat is: " + str(goal) + "\n")


        while rolls <= rollslimit :
            random_num0 = random.choice(die1)
            random_num1 = random.choice(die2)
            print("The rolls you got were: " + str(random_num0) + " and " + str(random_num1))
            totaldie = random_num0 + random_num1
            sumofalldies += totaldie
            print("Sum of roll: " + str(totaldie))
            rolls += 1

            print("\nSum of all roles: " + str(sumofalldies))
            print("You needed to get: " + str(goal))

        if sumofalldies > goal:
            print("\nYOU WON BY LUCK")
        elif sumofalldies == goal:
            print("\nYOU DID NOT WIN OR LOSE")
        else:
            print("\nYOU LOST BY LUCK")