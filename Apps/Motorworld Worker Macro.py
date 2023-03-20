import pyautogui
import time
import keyboard
        
def cursorPosistion():
    print("Please place cursor on pack price! (2 Seconds)")
    time.sleep(2)
    clickLocation = pyautogui.position()
    
    return clickLocation

def macro(clickLocation):
    
    time.sleep(1)
    pyautogui.click(clickLocation)
    time.sleep(.5)
    pyautogui.press('escape')
    pyautogui.press('escape')

def startmenu():
    
    
    print ("deez")
    recursiveAnswer = input("Do you want the macro to run indefinetly? (Y/N): ")

    if recursiveAnswer.lower() == "n":
    
        clickAmount = int(input("Please enter amount of workers needed: "))
        clickLocation = cursorPosistion()
        print("\nHold 'f' key to stop macro!")
    
        for recursiveTimes in range(0, clickAmount):
    
            macro(clickLocation)
            
            if keyboard.is_pressed("f"):
                print("Have fun Playing!")
                    

    elif recursiveAnswer.lower() == "y":
        
        start = True
        clickLocation = cursorPosistion()
        print("\nHold 'f' key to stop the macro!")
        
        while start == True:
            
            macro(clickLocation)
            
            if keyboard.is_pressed("f"):
                print("Have fun Playing!")
                

startmenu()