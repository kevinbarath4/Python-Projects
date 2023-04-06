import keyboard
import time
import pyautogui


answer = input("Do you want to run the macro? (Y/N): ")

if answer.lower() == "y":

    print("Place mouse on needed screen! (2 Seconds)")
    print("\nHold 'f' key to stop macro!")
    
    while answer.lower() == "y":

        time.sleep(2)
        pyautogui.mouseDown()
        
        if keyboard.is_pressed('f'):
            pyautogui.mouseUp()
            print("Have fun Playing")
            break

else:
    print("Have fun Playing!")