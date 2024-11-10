from bb84_program_functions import *

cls()
with open('./opening_script.txt','r') as file:
    for line in file:
        line = line.rstrip('\n')
        if line == '~':
            pressEnter()
        elif line == '`':
            cls()
        else:
            printSleep(line)