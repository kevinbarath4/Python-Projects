import random

def rollio(money):
    goal = random.randint(20, 50)
    print(f"The number you need to beat is: {goal}")
    money -= 150
    if money < 0:
        print("Sorry! you are all out of money! You will be forced to pay yout Dues!")
        return money
    
    elif money > 0:
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

def bar(money):
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
    
    while True:
        
        ans = input("\nWould you like a drink? (Y/N): ")
        if ans.lower() == "n":
            break
        elif ans.lower() == "y":
            print("Here are the available drinks and their prices:\n")
            for name, price in drinks.items():
                print(f"{name} - {price}$")
            ans = input("\nWhat would you like to drink? (type 'Leave' to exit): ")
            if ans.lower() == "leave":
                break
            elif ans.lower() in drinks:
                price = drinks[ans]
                if money >= price:
                    print(f"You ordered {ans} for {price}$")
                    money -= price
                else:
                    print("Sorry, you don't have enough money for that.")
            else:
                print("Sorry, I don't know that drink.")
        else:
            print("Invalid input.")

    print(f"You have {money}$ left.")

def startMenu():
    
    print("Welcome to Kevin's Kasino!")
    money = 1000
    while True:
        print(f"\nYou have {money}$.")
        ans = input("What would you like to do? (1 - Rollio, 2 - Bar, 3 - Leave): ")
        if ans == "1":
            money = rollio(money)
        elif ans == "2":
            bar(money)
        elif ans == "3":
            print("Cya Next Time!")
            break
        else:
            print("Invalid input.")

startMenu()
