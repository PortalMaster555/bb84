import time # for sleep()
import os

defaultLineDelay = 1
autoAdvance = False

# FUNCTIONS
def cls(): # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def printSleep(printString):
    print(printString)
    time.sleep(defaultLineDelay)

def pressEnter():
    if not autoAdvance:
        input("...")
    else:
        print("...")